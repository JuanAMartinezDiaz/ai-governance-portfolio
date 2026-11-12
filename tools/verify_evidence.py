"""Regenerate deterministic evidence, or check saved evidence without rewriting it."""
import argparse
import hashlib
import json
import re
from pathlib import Path

from control_lifecycle import run_lifecycle, render_markdown
from evaluate import evaluate
from governance import classify_with_trace, risk_score, validate_inventory

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def assert_narrative_consistency():
    """Tie the original Markdown arithmetic to its structured source fixtures."""
    risk_fixture = read_json("fixtures/risk-register.json")
    rows = {}
    for line in (ROOT / risk_fixture["source_document"]).read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > 4 and re.fullmatch(r"R\d+", cells[1]):
            match = re.search(r"(\d+)\s*[×x]\s*(\d+)\s*=\s*(\d+)", cells[3])
            if match:
                rows[cells[1]] = tuple(map(int, match.groups()))
    expected = {r["risk_id"]: (r["likelihood"], r["impact"],
                               risk_score(r["likelihood"], r["impact"])[0])
                for r in risk_fixture["risks"]}
    if rows != expected:
        raise ValueError("Risk table arithmetic differs from fixtures/risk-register.json")
    incident = read_json("fixtures/incident-evaluation.json")
    text = (ROOT / incident["source_document"]).read_text(encoding="utf-8")
    counts = {name: (int(selected), int(total)) for selected, total, name in
              re.findall(r"(\d+)\s+of\s+(\d+)\s+(?:applications\s+)?in\s+cluster\s+([A-Z])", text)}
    expected_counts = {r["id"]: (r["approved"], r["applications"])
                       for r in (incident["reference_cluster"], incident["compared_cluster"])}
    if counts != expected_counts:
        raise ValueError("Incident narrative counts differ from fixtures/incident-evaluation.json")


def governance_trace():
    paths = ["project-01-ai-system-inventory/inventory.json",
             "project-02-risk-assessment/synthetic-evaluation.json",
             "fixtures/risk-register.json", "fixtures/incident-evaluation.json",
             "tools/governance.py", "tools/evaluate.py",
             "project-02-risk-assessment/risk-assessment.md",
             "project-04-incident-response/incident-scenario.md"]
    rows = validate_inventory(read_json(paths[0]))
    risks = read_json("fixtures/risk-register.json")
    return {"evidence_scope": "bounded_synthetic_rules_with_explicit_inputs_and_reasons",
            "rule_revision": "bounded-triage-v1",
            "input_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
            "classifications": [{"system_id": r["id"], "source": paths[0],
                                 **classify_with_trace(r)} for r in rows],
            "risk_input_trace": [{**r, "calculated_score": risk_score(r["likelihood"], r["impact"])[0],
                                  "calculated_band": risk_score(r["likelihood"], r["impact"])[1]}
                                 for r in risks["risks"]],
            "limits": ["Presence and hashes do not establish truth, signatures, or immutable evidence.",
                       "The classifier implements only explicitly modeled exercise categories.",
                       "No legal clearance or operational control assurance follows from these checks."]}


def expected_artifacts():
    assert_narrative_consistency()
    lifecycle = run_lifecycle()
    def encoded(value):
        return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    return {"verification-output.json": encoded(evaluate()),
            "evidence/governance-trace.json": encoded(governance_trace()),
            "evidence/control-lifecycle.json": encoded(lifecycle),
            "evidence/control-lifecycle.md": render_markdown(lifecycle)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the four committed evidence artifacts")
    args = parser.parse_args()
    errors = []
    for path, expected in expected_artifacts().items():
        target = ROOT / path
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding="utf-8")
            print("WROTE", path)
        elif not target.exists() or target.read_text(encoding="utf-8") != expected:
            errors.append(path)
    if errors:
        print("FAIL: missing or stale generated evidence: " + ", ".join(errors))
        print("Review the changes, then run python3 tools/verify_evidence.py --write")
        return 1
    if not args.write:
        print("PASS: all four evidence artifacts match regenerated output; narrative arithmetic agrees with fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
