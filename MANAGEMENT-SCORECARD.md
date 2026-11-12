# Management scorecard — decisions, evidence and follow-up

**Fictional HarborBridge · design and fixture snapshot · 12 November 2026**

This is a proposed committee reporting pack. Its populated values come from identified portfolio fixtures or assumed business-case arithmetic. **No production monitoring, actual committee meeting, achieved benefit or effective operational control is represented.** Proposed thresholds below are exercise design choices, not approved policy or legal safe harbors.

## Decisions for the scenario committee

1. **Retain the CandidateRank live-deployment HOLD.** The C1–C8 release evidence remains incomplete; a passing arithmetic test is not model validation or proof of a control operating.
2. **Evaluate extraction-only as a separate option.** The base business case suggests capacity value, but slower verification or lower volume can erase it. No deployment or expenditure is authorized by this document.
3. **Require evidence-linked reporting.** Each owner should provide the numerator, denominator, period, source, limitations and action. Missing data appears as **unmeasured**, never as a green indicator or zero incidents.

## Current fixture snapshot

| Measure | Defined result and denominator | Evidence state and interpretation | Source |
| --- | --- | --- | --- |
| Inventory records with named owners | **10 / 10** supplied records have a nonempty `owner` field | Fixture completeness only; does not verify that an owner accepted accountability or that the inventory covers the enterprise | [Inventory](project-01-ai-system-inventory/inventory.json) |
| Inventory records with purpose and authority fields | **10 / 10** supplied records include both | Field presence is not confirmed scope or a permitted action | [Inventory](project-01-ai-system-inventory/inventory.json) |
| CandidateRank controls with accepted release evidence | **0 / 8** C1–C8 controls have complete accepted operational evidence | C1 has synthetic arithmetic only; C2–C8 tests are not run. All eight require further evidence | [Risk assessment and evidence conditions](project-02-risk-assessment/risk-assessment.md) |
| Synthetic recruitment selection comparison | A: **60 / 100**; B: **36 / 100**; B/A: **0.60**; difference: **−24 percentage points** | Invented aggregate counts; exercise alert calls for investigation. No causal or legal conclusion | [Input fixture](project-02-risk-assessment/synthetic-evaluation.json), [verification](VERIFICATION.md) |
| Extraction-only capacity opportunity | **428 internal hours in year one**, versus 2,656 manual-process hours; includes 60 setup hours | Assumed arithmetic, not a measured reduction. No headcount or payroll savings | [Business case](business-case/README.md), [results](business-case/results.json) |
| Extraction-only first-year economic value | **$13,080** versus manual at 12,000 assumed applications | Internal capacity value less external costs; contingent on all assumptions and a future lawful, controlled operating scope | [Assumptions](business-case/assumptions.json), [results](business-case/results.json) |

## Proposed operating measures

| Measure and denominator | Proposed target / action trigger | Cadence and accountable owner | Required source and present evidence status |
| --- | --- | --- | --- |
| **Verified inventory coverage:** in-scope systems reconciled to an accepted owner and current purpose ÷ discovered in-scope systems | 100%; unresolved or unowned items escalated before approval | Weekly; business owners, governance office aggregates | Procurement, platform, access and use-case registers reconciled. **Unmeasured:** the ten-system fixture is not an enterprise denominator |
| **Release-control evidence coverage:** applicable required controls with reviewed, accepted evidence ÷ applicable required controls | 100% before release; missing mandatory evidence keeps the gate closed | At every release/change; business executive, independent validation and risk challenge | Versioned evidence index, test records and reviewer disposition. **Fixture 0/8 for CandidateRank** |
| **Overdue high/critical findings:** open high/critical findings past agreed due date ÷ open high/critical findings with due dates; also show counts | No overdue critical finding; any critical finding escalated immediately; high findings tracked to agreed due dates | Weekly and on material change; finding owner, second-line challenge | Finding register, owners, due dates and closure evidence. **Unmeasured:** no operating issue register supplied; if denominator is zero, show “not applicable,” not 0% |
| **Exception expiry:** active risk exceptions beyond expiry ÷ active exceptions | Zero expired exceptions; suspend the exception or seek a new authorized decision before continued use | Daily expiry check; business risk owner | Approval identity, scope, conditions, expiry and revocation record. **Unmeasured:** no actual exceptions or approvals |
| **Governance decision time:** median and 90th percentile business days from complete intake to decision; report pending case count/age separately | Establish baseline; provisional objective ≤10 business days for standard cases, with enhanced cases separately scoped | Monthly; governance office | Timestamped intake and decision records; no resetting the clock by closing/reopening. **Unmeasured** |
| **Verified review quality:** material errors found by independent reference review ÷ reviewed case sample, disaggregated where appropriate | Predefine acceptance with validation; any critical error blocks release; investigate group disparities and uncertainty | Per evaluation/release; independent validation lead | Matched review records, adjudication, sample rationale and uncertainty. **Unmeasured:** synthetic 0.60 ratio is an alert fixture, not an error metric |
| **Human effort and exception burden:** direct review + rework + exception + governance hours; show cases, exception count and minutes per case | Test the business-case assumptions; no benefit credited until observed and quality gates met | Per evaluation, then monthly if approved; HR executive | Task/time observations and expense records. **Modeled only:** see three-alternative comparison |
| **Material-change review:** observed material model/prompt/tool/data/authority changes assessed before use ÷ all observed material changes | 100%; unapproved changes quarantined pending reassessment | On change; technology executive | Version inventory, change records, independent test and approval evidence. **Unmeasured** |
| **Incident containment and recovery:** time from credible alert to containment; time to authorized restart; number of affected cases | Severity-specific targets set by the incident plan; no restart before agreed evidence | Per incident and monthly trends; incident commander | Alert/action timestamps, preserved evidence and restart authorization. **Tabletop design only; no live incident metrics** |
| **Benefit realization:** observed net economic value ÷ approved business-case value; report capacity hours separately | Reassess when value falls below the approved tolerance or effort/quality degrades | Monthly after an authorized release; HR and Finance | Verified effort, volumes, invoices, quality outcomes and attributable baseline. **Unmeasured:** no approved or realized benefit |

## Interpretation rules

- Keep **designed**, **executed**, **independently reviewed**, and **operating** evidence states separate. Software-test counts support only the code behavior those tests exercised.
- A blank numerator or absent denominator is **unmeasured**. Show excluded populations, scope changes and stale evidence; do not hide them in an aggregate score.
- Show residual-risk judgment and dissent beside any KPI. Strong throughput or economics cannot compensate for unlawful use, critical harm or absent release evidence.
- Business owners remain accountable for action and risk acceptance within their authority. Second-line risk challenges the evidence and escalates; internal audit provides independent assurance.

[Business case](business-case/README.md) · [Governance operating model](project-03-responsible-ai-policy/governance-operating-model.md) · [Portfolio](README.md)
