# Verification record

**Updated November 12, 2026.** Local verification was performed in a managed Linux workspace using Python. The governance and business-case checks use the standard library.

## Executed checks

| Command | Observed result |
| --- | --- |
| `python3 -m unittest discover -s tests -v` | 24 governance and control-lifecycle tests passed. |
| `python3 tools/verify_evidence.py` | Four generated evidence artifacts matched; structured inputs agreed with risk and incident narrative values. |
| `python3 -m unittest discover -s business-case -p 'test_*.py' -v` | 8 business-case tests passed. |
| `python3 business-case/evaluate.py --check` | Saved results matched deterministic calculations. |
| `python3 tools/check_links.py` | All local linked-file targets resolved. External URLs and anchor names are outside this check. |

**Total: 32 automated tests passed locally.** The [GitHub Actions workflow](https://github.com/JuanAMartinezDiaz/ai-governance-portfolio/actions/workflows/portfolio-evidence.yml) records verification for each published revision. A dated local result does not establish that later revisions pass.

## What the evidence shows

- The original ten-system evaluator results are preserved in [verification-output.json](verification-output.json): three high-risk cases, one prohibited scenario on the supplied facts, four without an identified high-risk category within scope, and two requiring review.
- The recruitment example computes 60% and 36% selection rates, ratio 0.60, and a difference of -24 percentage points.
- The incident example computes 50% and 30% selection rates, ratio 0.60, and a difference of -20 percentage points.
- One critical, six high, and one moderate risk are recorded. Current residual scores receive no credit for untested operational controls.
- The [trace output](evidence/governance-trace.json) binds source inputs to rule identifiers, explanations, and evidence requirements.
- The [control lifecycle](evidence/control-lifecycle.md) records a deliberately weak baseline accepting eight unsafe proposed outputs. The strict contract retest accepts two clean outputs and rejects all eight unsafe outputs. Version and scope changes block previously clean output; revocation prevents reuse.
- The [business case](business-case/README.md) computes modeled outcomes from disclosed assumptions, including adverse sensitivities and capacity constraints. It measures no actual pilot or achieved savings.

## Scope of the new executable example

`SYN-EXTRACT-001` is a separate, deterministic, extraction-only fixture. It uses invented trusted records and proposed outputs. The program tests an exact output contract and a simulated decision lifecycle. It does not run an LLM or discover prompt injection in arbitrary text. The ten-case fixture does not substitute for the planned 50-case operational model test in C6.

A machine-generated limited-approval state permits only rerunning the same synthetic fixture. It is not human authorization, legal clearance, approval of CandidateRank or HiringAssist, or permission to deploy. Input hashes identify changes; they are not signatures or immutable audit storage.

## Review limits

No vendor recruitment or credit model, authenticated enterprise approval service, external execution gateway, immutable logging service, or live monitoring service was tested. No human tabletop participants were convened. No legal opinion, certification, or conformity assessment was obtained. No employer or customer information was used, and no human signatures or approvals were fabricated.

The written case studies include completed analysis of fictional facts and proposed operational controls. HB-003 and HB-011 remain on hold for live use. Juan's personal walkthrough and any independent practitioner critique are tracked in [AUTHORSHIP.md](AUTHORSHIP.md) and [INTERVIEW.md](INTERVIEW.md).

## Reproduction and maintenance

Run the commands above from the repository root with Python 3.10 or newer. No network, model download, API key, paid service, or additional Python package is required for these checks.

`python3 tools/verify_evidence.py --write` regenerates evidence after an intentional source change. Review the resulting changes before committing them. The checker independently compares risk-table arithmetic and incident counts to structured fixtures.

The optional employer PDF has an editable generator in [presentation/build_employer_brief.py](presentation/build_employer_brief.py). Rebuilding that PDF requires ReportLab; it is not a dependency of the governance tests. The final PDF was rendered and visually inspected.

## Historical baseline

The November 10 edition recorded 14 passing tests. Its original [source revision](https://github.com/JuanAMartinezDiaz/JuanAMartinezDiaz/tree/7e7e6e56bf544578643d8927cfb3c757d4b247de/ai-governance-portfolio) remains available. November 12 adds traceability, the bounded control lifecycle, scenario business-case tests, continuous verification, and clearer employer navigation without changing the original evaluator values.
