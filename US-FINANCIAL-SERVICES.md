# Applying the portfolio in US financial services

**Transfer note · official sources checked 12 November 2026.** The five cases use fictional EU facts. Their control disciplines can inform US banking work, while legal classification and supervisory applicability require a separate assessment of the institution, activity, technology and regulator. An EU high-risk category is not a US classification.

## Current model-risk baseline

The Federal Reserve's [SR 26-2, issued 17 April 2026](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), supersedes SR 11-7 and SR 21-8. Use the revised guidance when assessing its scope rather than treating the 2011 letter as the current standard. It emphasizes tailoring to the organization's model risk, size and complexity and is expected to be most relevant above $30 billion in assets.

The [OCC's accompanying bulletin](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html) explicitly excludes generative and agentic AI from this guidance. It also excludes simple arithmetic and deterministic rule-based processes without the relevant statistical, economic or financial theories. The guidance is not an enforceable standard. Therefore the small portfolio calculators and output-contract demonstration are **not model validation under SR 26-2**. Traditional or non-generative model use needs its own scope assessment; GenAI and agent workflows still need appropriate institutional risk governance and applicable legal controls.

## Transfer to an existing bank program

| Existing discipline | Portfolio evidence to inspect | Bank-specific adaptation |
| --- | --- | --- |
| AI/use-case inventory | [Operational register](project-01-ai-system-inventory/operational-register.md) | Link business service, legal entity, system owner, supplier, model/tool versions and action authority to the bank's existing inventories |
| RCSA and control assessment | [Risk assessment](project-02-risk-assessment/risk-assessment.md) | Map risk event, cause and consequence to control objective, owner, test evidence and issue record; do not credit untested controls |
| Independent risk challenge | [Operating model](project-03-responsible-ai-policy/governance-operating-model.md) | Use existing first/second/third-line responsibilities and delegated authorities; preserve dissent and escalation |
| Model-risk interface | [Evidence needed for C1–C8](project-02-risk-assessment/risk-assessment.md) | Determine applicable model scope and required expertise; distinguish statistical validation from workflow/security controls |
| Third-party risk | [Mock supplier review](project-05-high-risk-documentation/mock-supplier-review.md) | Align diligence, contracts, ongoing monitoring, change notices and exit arrangements with the actual relationship and its risk |
| Information security and change | [Bounded lifecycle evidence](evidence/control-lifecycle.md) | Test identity, data/tool permissions, version changes, logging and revocation in the real execution environment |
| Incidents and customer impact | [Incident manifest and reporting log](project-04-incident-response/evidence-and-reporting-log.md) | Integrate existing incident, complaint, remediation, continuity and regulatory-notification processes; assess actual reporting rules |
| Management oversight | [Management scorecard](MANAGEMENT-SCORECARD.md) | Set risk appetite, meaningful denominators, escalation thresholds and accountable remediation resources |

This table is a proposed operating connection, not evidence of a working integration with a bank or commercial GRC platform.

## Supplier-guidance status

[SR 23-4](https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm) provides the 2023 interagency third-party relationship guidance. A replacement is currently [proposed, OP-1881](https://www.federalreserve.gov/apps/proposals/FR-2026-0031-01/details), with comments due 16 November 2026. The proposal is not presented here as final. Recheck its disposition before relying on this note in an actual engagement.

## Practical bank example: control-evidence assistance

For a synthetic RCSA workflow, an assistant may extract control descriptions and cite evidence for a human review. It must not attest control effectiveness, accept residual risk, close an independent issue, change its permissions or submit an authoritative report on its own. A missing source, version mismatch, unauthorized record or unsupported claim returns the item for review. This is a proposed application of the portfolio's reasoning; no employer data or deployed banking integration is used.

The [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) supplies a voluntary structure for this work. Its outcome mappings in [TRACEABILITY.md](TRACEABILITY.md) are selected design alignments, not certification. Legal/compliance must separately assess the relevant privacy, employment, consumer/lending, security and records obligations for any real use.
