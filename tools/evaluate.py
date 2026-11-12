"""Run synthetic examples; prints deterministic JSON and contacts no services."""
import json
from pathlib import Path
from governance import classify, selection_analysis, risk_score, validate_inventory

ROOT = Path(__file__).resolve().parents[1]

def evaluate():
    inventory = validate_inventory(json.loads((ROOT / "project-01-ai-system-inventory/inventory.json").read_text()))
    fixture = json.loads((ROOT / "project-02-risk-assessment/synthetic-evaluation.json").read_text())
    a, b = fixture["group_a"], fixture["group_b"]
    risks = json.loads((ROOT / "fixtures/risk-register.json").read_text())["risks"]
    incident = json.loads((ROOT / "fixtures/incident-evaluation.json").read_text())
    q, p = incident["reference_cluster"], incident["compared_cluster"]
    return {
        "evidence_scope": "synthetic_rule_and_arithmetic_checks_only",
        "classifications": [{"id": r["id"], "result": classify(r)} for r in inventory],
        "recruitment": selection_analysis(a["applicants"], a["selected"], b["applicants"], b["selected"], fixture["internal_alert_ratio"]),
        "incident_reference_Q_compared_with_P": selection_analysis(q["applications"], q["approved"], p["applications"], p["approved"], incident["internal_alert_ratio"]),
        "risk_scores": [{"risk": r["risk_id"], "score": risk_score(r["likelihood"], r["impact"])[0], "band": risk_score(r["likelihood"], r["impact"])[1]} for r in risks]
    }

if __name__ == "__main__":
    print(json.dumps(evaluate(), indent=2, sort_keys=True))
