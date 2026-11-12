# Project 2 — Recruitment risk assessment

**Synthetic worked review of HB-003 CandidateRank v0.9.** Intended use: score and rank applicants for analyst roles at HarborBridge's EU operation. Vendor: fictional HarborModels. The HR executive wants a live pilot. No actual vendor model is available.

Artifacts: [risk assessment](risk-assessment.md), [executive memo](governance-review-memo.md), and [synthetic inputs](synthetic-evaluation.json). Reproduce the arithmetic with `python3 tools/evaluate.py` from the portfolio root.

Recommendation: hold live use; allow only an isolated synthetic evaluation. The numerical exercise demonstrates measurement and challenge, not model performance or a legal finding. A complete assessment can reach a negative decision.

**Read the decision in five minutes:** [executive memo](governance-review-memo.md) → [business tradeoffs](../business-case/README.md) → [bounded control finding and retest](../evidence/control-lifecycle.md). The retest concerns a separate non-ranking extraction fixture; it does not clear CandidateRank's live-use hold.
