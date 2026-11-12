# Incident evidence manifest and reporting decision log

**IR-001 · written tabletop supplement · 12 November 2026.** Scenario clocks below describe the fictional exercise. No operational collection, tabletop meeting, legal signoff or external notification occurred.

## Evidence manifest

| ID | Material expected in a real investigation | Material actually available here | Custodian role / integrity requirement |
| --- | --- | --- | --- |
| E-IR-01 | Implicated model, feature transform and configuration versions | Narrative assumption only; no model bytes | Engineering custodian; preserve original version before modification |
| E-IR-02 | Decision-level inputs, outputs, timestamps and reviewer actions | No applicant-level records | Data custodian; controlled export, lawful scope and custody history |
| E-IR-03 | Approval identity, authority, scope and change history | Fictional change described in the [scenario](incident-scenario.md) | Governance records owner; verify provenance and authorization |
| E-IR-04 | Detection query, population definition and reconciled counts | Invented aggregate counts: P 60/200; Q 150/300 | Validation; independently reconcile before population or harm claims |
| E-IR-05 | Complaint and notices | Fictional complaint summary only | Customer-remediation lead; restrict access and preserve originals |
| E-IR-06 | Access and transfer audit | No real collection or transfers | Evidence custodian; separately protected audit trail |

No collection times, hashes, signatures or chain-of-custody events are invented. In an operational incident, record collector identity, source, collection time, byte-level digest, destination, every transfer and access authorization. A matching hash alone does not authenticate the source or defeat replacement by a privileged actor.

## Worked reporting decision log

| Scenario checkpoint | Known facts and uncertainty | Recorded disposition / next decision |
| --- | --- | --- |
| Detection, 09:00 | Aggregate approval-rate difference and alleged explanation failure; query, qualifications and causality unresolved | Record earliest awareness; open incident; preserve model and decision evidence |
| First hour | Potential credit harm at scale; no established legal serious-incident conclusion | Escalate to Legal/compliance and provider contact role; prepare preliminary facts; do not wait for final RCA |
| Initial legal triage | EU use is assumed; actual jurisdiction, statutory trigger and responsible reporting entity need resolution | Separate the deployer's Article 26 duties from provider Article 73 reporting; record the trigger and clock for each applicable obligation |
| If risk or serious-incident conditions are established | Applicable legal duties may require urgent suspension and notification | Reporting owner follows the applicable immediate/without-undue-delay duties; outer limits are not permission to delay |
| Incomplete evidence | Cause and affected population remain uncertain | Update facts and preliminary report where required; record uncertainty; retain reporting and remediation owners |

The owner must identify the actual competent authority and any sector-specific reporting overlap before sending. This exercise supplies neither an invented recipient nor a completed filing. The [official Article 26 text](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26) and [Article 73 text](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-73) support the distinctions; legal applicability requires current facts and source review.

## Next exercise acceptance

Conduct a timed exercise with actual participants: verify stop permissions, manual queue capacity, retrieval of preserved evidence, provider unavailability, clock ownership and a restart refusal when evidence is missing. Record observed timings and failures. Until that happens, these remain proposed operational tests, and the [RCA hypotheses](root-cause-analysis.md) remain unproven.
