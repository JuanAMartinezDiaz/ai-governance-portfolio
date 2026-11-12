# CandidateRank alternatives — business case

**Decision BC-003 · fictional HarborBridge · 12 November 2026**  
**Evidence:** deterministic calculations from invented assumptions. No actual model, applicant, pilot, savings or workforce outcome is measured.

## Executive recommendation

**Keep CandidateRank on HOLD. Retain structured human screening while evaluating an extraction-only alternative in an isolated synthetic exercise.** The economic comparison does not grant deployment authority. CandidateExtract needs its own purpose, downstream-influence, privacy, security and validation review; removing ranking does not establish exemption or safety.

In all three alternatives, trained HR reviewers inspect the underlying applications and make every screening decision. The proposed tools cannot reject or contact applicants, make offers, or hide records from review. These are evaluation-scope requirements; enforcement has not been demonstrated.

At the base assumptions, reviewer-first ranking **increases** human effort because reviewers still assess each application independently and then challenge the ranking. Extraction-only could release **428 internal staff hours in the first operating year**, after setup, with **$13,080 of modeled net economic value**. Its case disappears if extraction verification takes too long or volume is too low. These are hypotheses worth testing, not achieved benefits.

| Calculated measure | Existing manual process | Reviewer-first ranking | Extraction only |
| --- | ---: | ---: | ---: |
| Internal human effort / month | 221.33 hours | 270.67 hours | 180.67 hours |
| Assumed monthly rework events | 40 | 40 | 40 |
| Assumed monthly exception events | 60 | 80 | 80 |
| Estimated monthly-batch completion | 15.58 business days | 18.42 business days | 12.92 business days |
| Recurring economic cost / month | $13,280 | $16,740 | $11,140 |
| Upfront economic cost | $0 | $19,800 | $12,600 |
| First-year economic cost, including setup | $159,360 | $220,680 | $146,280 |
| First-year economic value versus manual | Baseline | **−$61,320** | **+$13,080** |
| First-year internal capacity versus manual | Baseline | **−672 hours** | **+428 hours** |
| Current scenario decision | Retain existing process | **HOLD** | **ASSESS; no live approval** |

Source: [assumptions](assumptions.json), [calculator](evaluate.py), and [saved results](results.json). The outputs use full precision internally; displayed hours are rounded.

### What “value” means here

Time, effort and cost are different measures. **Elapsed time** estimates when a monthly batch finishes. **Internal effort** totals person-hours across review, rework, exceptions, governance and setup. **Economic cost** values that effort at an assumed blended rate and adds supplier and assurance charges.

Extraction's first-year 428 hours represents capacity potentially available for reassignment. At $60/hour that is $25,680 of internal capacity value; deducting $12,600 of additional external charges leaves $13,080. **No salary reduction, headcount removal or cash saving is assumed.** Vendor/assurance personnel hours are not available and are represented by fees, so internal hours are not the total human effort across all organizations.

## Assumptions that drive the decision

The exercise assumes 1,000 applications per month, 12 operating months, a $60 fully loaded blended internal hourly cost, two parallel reviewers, eight-hour business days, and 20 working days per month. Queue waiting is fixed at 16 business hours. The comparison begins **after any hypothetical approval**; approval delays and implementation elapsed time are not forecast.

| Input | Manual | Reviewer-first ranking | Extraction only |
| --- | ---: | ---: | ---: |
| Direct human review / application | 12 min | 14 min | 9 min |
| Correctable rework assumption | 4% × 8 min | 4% × 8 min | 4% × 10 min |
| Exceptions requiring extra handling | 6% × 12 min | 8% × 15 min | 8% × 12 min |
| Governance / monitoring effort per month | 4 hours | 12 hours | 8 hours |
| Batch compute delay | 0 hours | 2 hours | 1 hour |
| Platform fee per month | $0 | $500 | $300 |
| Internal setup effort | 0 hours | 80 hours | 60 hours |
| Supplier setup fee | $0 | $6,000 | $3,000 |
| Independent assurance provision | $0 | $9,000 | $6,000 |

All values are invented planning inputs, not market prices, vendor quotations or employer information. The existing manual process has no incremental setup charge. Ranking retains 12 minutes of independent assessment plus two minutes of comparison; extraction assumes verified structured fields reduce direct review to nine minutes. **No improvement in hiring quality is assumed.** The common 4% rework rate is an administrative correction workload, not observed model accuracy, a final error rate or evidence of fairness.

Rework corrects an identified record/preparation error; exception handling resolves a separate ambiguity or accommodation issue. A case may have both, but the time allowances cover distinct tasks. Undetected errors, job validity, applicant harm, accessibility and disparate outcomes remain unmeasured. The [risk assessment](../project-02-risk-assessment/risk-assessment.md) governs those questions.

## Reproduce the comparison

Python 3.10+ and the standard library are sufficient. From the repository root:

```bash
python3 business-case/evaluate.py --check
python3 -m unittest discover -s business-case -p 'test_*.py' -v
```

`--check` recalculates the base and sensitivity cases and compares them with `results.json`. To examine an alternative assumption, edit `assumptions.json`, run `python3 business-case/evaluate.py`, and review the change. `--write` regenerates the saved results. No model, network service or personal data is involved.

### Formulas

For monthly volume **N**, review minutes **m**, rework rate **r** and time **tᵣ**, exception rate **e** and time **tₑ**, governance hours **g**, hourly cost **w** and platform fee **p**:

- Casework hours = N × (m + r × tᵣ + e × tₑ) ÷ 60.
- Monthly internal effort = casework hours + g.
- Monthly economic cost = monthly internal effort × w + p.
- Upfront cost = internal setup hours × w + supplier setup fee + independent assurance provision.
- First-year economic cost = 12 × monthly economic cost + upfront cost.
- First-year internal capacity released = 12 × (manual monthly effort − alternative monthly effort) − incremental internal setup hours.
- Batch completion in business days = (queue wait + compute delay + casework hours ÷ parallel reviewers) ÷ hours per business day.

The elapsed-time estimate is a simple batch-workload model, not a queue simulation or service-level prediction. It assumes casework can be evenly divided, with no new arrivals during that batch, and governance work occurs outside the review critical path. At high volume, a fixed queue assumption becomes unrealistic; the calculator flags batches that exceed the monthly window. It does not automatically add staff or claim feasible throughput.

## Sensitivity: when extraction stops paying

Each row varies one input while holding the others at base values. These are decision sensitivities, not probabilities or confidence intervals.

| Input varied | Values compared | Calculated first-year value versus manual |
| --- | --- | --- |
| Monthly volume | 500 / 1,000 / 2,000 applications | −$3,000 / +$13,080 / +$45,240* |
| Blended labor value | $40 / $60 / $90 per hour | +$4,520 / +$13,080 / +$25,920 |
| Direct extraction review | 8 / 9 / 12 minutes | +$25,080 / +$13,080 / **−$22,920** |
| Correctable rework rate | 2% / 4% / 8% | +$15,480 / +$13,080 / +$8,280 |
| Exception rate | 4% / 8% / 15% | +$18,840 / +$13,080 / +$3,000 |
| Independent assurance provision | $3,000 / $6,000 / $18,000 | +$16,080 / +$13,080 / +$1,080 |

*At 2,000 applications, extraction takes an estimated 23.71 business days with the fixed two-reviewer assumption and does not fit the 20-day monthly window. Its attractive arithmetic does not establish operational feasibility.*

At all other base inputs, extraction must take **less than 10.09 direct-review minutes per application** to produce positive first-year modeled value. Base setup payback is approximately **5.89 operating months**, conditional on the assumptions holding. Neither result overrides a failed safety, legal or control gate.

## Evidence required before any change in recommendation

HR should run the proposed [30-day synthetic evaluation](../project-02-risk-assessment/governance-review-memo.md) only within its authorized scope. Use matched fictional candidate packs and predefined job criteria; counterbalance review order and record each participant's task and start/stop times. Compare all three alternatives, including verification, rework, exceptions and governance overhead. Use an independent reference review to examine errors and accessibility; a pilot sample does not prove population performance.

Collect actual evaluation expenditure and supplier estimates; test the C1–C8 conditions; investigate any subgroup or job-validity concern; and record staff feedback and the remaining uncertainty. Recalculate this business case with traceable observations. **An economically attractive result is only one input to a new governance decision.** Until then, CandidateRank remains on HOLD and extraction remains an unapproved alternative.

[Management scorecard](../MANAGEMENT-SCORECARD.md) · [Risk assessment](../project-02-risk-assessment/README.md) · [Portfolio](../README.md)
