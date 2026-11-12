# Interview walkthrough and personal review

Prepared for Juan's review. These are discussion prompts, not a claim that he has already completed the walkthrough.

**Suggested route:** [Project 2 decision](project-02-risk-assessment/governance-review-memo.md), [business case](business-case/README.md), [bounded control finding/retest](evidence/control-lifecycle.md), then [Project 3 exception disposition](project-03-responsible-ai-policy/worked-exception.md). The [authorship record](AUTHORSHIP.md) distinguishes preparation and automated review from personal acceptance.

## Three-minute explanation

“This portfolio follows a fictional financial institution from discovering AI use to making a release decision. The inventory separates legal classification from business risk. The recruitment review shows why a vendor's accuracy claim is insufficient. The operating model gives the business ownership and risk an independent challenge role. The incident case preserves evidence before changing the model. The replacement-system packet keeps deployment blocked where evidence is missing.”

## Questions to defend

1. Why is a fraud-detection use case treated differently from creditworthiness assessment? Explain the stated purpose and why reuse can change the classification.
2. Why is a person approving a shortlist insufficient? Explain ranking influence, automation bias, and how a reviewer can discover omitted candidates.
3. What does the 0.60 selection-rate ratio establish? Reproduce the arithmetic, then explain why it does not establish cause or legal discrimination.
4. Who owns residual risk? Distinguish the accountable business executive from independent risk challenge and internal audit assurance.
5. Why is a target risk score not the current residual score? Identify the evidence needed before crediting a control.
6. What can happen in the first hour of an incident? Discuss stopping new decisions, preserving configuration and outputs, and keeping customers served through a manual process.
7. Why can a completed documentation exercise legitimately conclude “do not deploy”? Identify absent supplier evidence and the difference between designed controls and tested controls.
8. How does an EU example help in a US banking role? Discuss transferable inventory, ownership, challenge, testing, and incident disciplines while keeping legal applicability separate.
9. Why might reviewer-first ranking consume its proposed time saving? Explain the [business-case assumptions](business-case/README.md), human effort, rework and the narrower extraction alternative without claiming achieved savings.
10. What did the C6 review find? Explain how altered ranking could pass a tool-action/leakage-only test, what the local extraction contract actually checks, and why the full model suite remains unrun.
11. Why does `SIMULATED_LIMITED_APPROVAL` not authorize live hiring? Identify `SYN-EXTRACT-001`, the fictional trusted inputs, the scope/version invalidation, absent human authorization and the continuing HB-003/HB-011 holds.
12. What changed in US model-risk guidance? Explain the [SR 26-2 scope note](US-FINANCIAL-SERVICES.md), the generative/agentic exclusion, and why broader banking governance still needs a separate applicability assessment.

## Review record

| Item | Status |
| --- | --- |
| AI-assisted artifacts and executable examples created | Complete; see verification |
| Automated content and technical review | Recorded for this revision; see verification and traceability |
| Juan has reviewed decisions and adjusted wording to his own judgment | Pending |
| Juan has rerun the checks and explained the results | Pending |
| Independent practitioner critique | Not obtained |
| Real-world implementation, certification, or regulatory approval | Not claimed |

Recommended next step: personally review the Project 2 hold decision and Project 3 authority model, record any disagreement in a dated commit, and practice defending the decisions without reading the documents. That produces stronger evidence of judgment than adding more templates.

## Personal review record to complete after the walkthrough

Record the date and revision reviewed, decisions challenged, changes requested, checks personally reproduced, limitations explained and any unresolved questions. Keep this section pending until that review occurs. Permission to publish, a passing script or AI-generated commentary does not establish personal completion.
