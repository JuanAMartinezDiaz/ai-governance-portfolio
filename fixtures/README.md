# Synthetic fixture inputs

These files are deliberately invented inputs for reproducible exercises. They contain no employer data, real applicants, model responses, human approvals, or measured business results.

| File | Purpose | Evidence produced |
| --- | --- | --- |
| [risk-register.json](risk-register.json) | R1–R8 ordinal inputs and control IDs, checked against the risk table | [Original arithmetic](../verification-output.json) and [source trace](../evidence/governance-trace.json) |
| [incident-evaluation.json](incident-evaluation.json) | Invented P/Q approval counts, checked against the incident narrative | [Original arithmetic](../verification-output.json) |
| [control-lifecycle.json](control-lifecycle.json) | Two trusted invented records and ten proposed extraction outputs | [Control lifecycle](../evidence/control-lifecycle.md) |

The original [inventory](../project-01-ai-system-inventory/inventory.json) and [recruitment counts](../project-02-risk-assessment/synthetic-evaluation.json) remain the inputs for their existing examples.

## Reproduction

Run `python3 -m unittest discover -s tests -v` and `python3 tools/verify_evidence.py` from the repository root. After an intentional input or control change, inspect the differences and use `python3 tools/verify_evidence.py --write` to regenerate committed evidence. A changed hash identifies a changed input; it does not prove source truth or provide an authenticated signature.

## Contract boundaries

The lifecycle exercise accepts only exact facts from the requested trusted synthetic record. It excludes ranking, recommendations, changed job criteria, other candidates' data, and tool actions. It tests a deterministic output validator against known cases. It does not test an LLM, document ingestion, real-world identity controls, or the full planned operational adversarial suite. Its approval and revocation states are machine simulations for this fixture only.
