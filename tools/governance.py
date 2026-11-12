"""Bounded educational triage, not a comprehensive legal classifier."""
import math
from datetime import date

HIGH_RISK = "HIGH_RISK"
REVIEW = "REVIEW_REQUIRED"
NONE = "NO_HIGH_RISK_CATEGORY_IDENTIFIED"
PROHIBITED = "PROHIBITED_ON_STATED_FACTS"


def classify_with_trace(record):
    """Explain the narrow exercise rule; never infer legal clearance."""
    def result(decision, rule_id, reason, required_evidence):
        return {"decision": decision, "rule_id": rule_id, "reason": reason,
                "required_evidence": required_evidence}

    if not isinstance(record, dict):
        return result(REVIEW, "SCOPE-001", "Input is not a structured system record.",
                      ["A complete inventory record and verified territorial scope"])
    if record.get("eu_scope") is not True:
        return result(REVIEW, "SCOPE-001", "EU scope is absent, uncertain, or outside this exercise.",
                      ["Applicable jurisdiction and assessment by the accountable reviewer"])
    purpose = record.get("purpose_code")
    if purpose == "workplace_biometric_emotion":
        if record.get("medical_safety_exception") is False:
            return result(PROHIBITED, "EMOTION-001", "Stated workplace biometric emotion use has no medical or safety exception.",
                          ["Stop proposed use; legal review of the stated facts"])
        return result(REVIEW, "EMOTION-002", "An exception claim requires additional facts and review.",
                      ["Evidence supporting the claimed medical or safety purpose"])
    if purpose in {"natural_person_creditworthiness", "candidate_ranking", "life_insurance_pricing"}:
        return result(HIGH_RISK, "CATEGORY-001", "Stated purpose matches a modeled high-risk category.",
                      ["Use-specific risk assessment, control evidence, and accountable release decision"])
    if purpose == "fraud_detection_only":
        if record.get("credit_decision_reuse") is False:
            return result(NONE, "FRAUD-001", "Stated use is fraud detection only, with credit-decision reuse excluded.",
                          ["Confirm purpose boundary and assess security, privacy, and operational risks"])
        return result(REVIEW, "FRAUD-002", "Credit-decision reuse is present or unresolved.",
                      ["Document downstream decisions and reassess the changed purpose"])
    if purpose in {"faq_only", "internal_policy_retrieval", "payment_draft_only"}:
        if record.get("boundary_confirmed") is True:
            return result(NONE, "BOUNDARY-001", "No high-risk category is identified within the stated bounded exercise use.",
                          ["Maintain stated authority boundaries and assess other applicable controls"])
        return result(REVIEW, "BOUNDARY-002", "The proposed operational boundary is not confirmed.",
                      ["Evidence of actual data, tool, and decision authority"])
    # Preparatory work and infrastructure need facts outside this narrow model.
    return result(REVIEW, "UNKNOWN-001", "The narrow exercise does not resolve this purpose.",
                  ["Additional facts and specialist classification review"])


def classify(record):
    return classify_with_trace(record)["decision"]


def validate_inventory(records):
    """Check basic accountability fields; field presence is not proof of truth."""
    required_text = ("id", "name", "purpose_code", "owner", "vendor_version", "data",
                     "authority", "evidence_state", "review_date", "review_trigger")
    if not isinstance(records, list) or not records:
        raise ValueError("Inventory must be a nonempty list")
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Every inventory entry must be an object")
        for key in required_text:
            if not isinstance(record.get(key), str) or not record[key].strip():
                raise ValueError(f"Missing or empty inventory field: {key}")
        if record["id"] in seen:
            raise ValueError(f"Duplicate system ID: {record['id']}")
        seen.add(record["id"])
        if type(record.get("eu_scope")) is not bool:
            raise ValueError("eu_scope must be an explicit boolean in the fixture")
        if record.get("internal_risk") not in {"low", "moderate", "high", "critical", "unresolved"}:
            raise ValueError("internal_risk is missing or unknown")
        date.fromisoformat(record["review_date"])
        for key in ("credit_decision_reuse", "medical_safety_exception", "boundary_confirmed"):
            if key in record and type(record[key]) is not bool:
                raise ValueError(f"{key} must be a boolean when present")
    return records


def selection_analysis(a_total, a_selected, b_total, b_selected, alert_ratio=0.8):
    values = (a_total, a_selected, b_total, b_selected)
    if any(type(v) is not int for v in values):
        raise ValueError("Counts must be integers, not booleans or inferred values")
    if min(a_total, b_total) <= 0 or not 0 <= a_selected <= a_total or not 0 <= b_selected <= b_total:
        raise ValueError("Counts must describe nonempty populations and valid selections")
    if type(alert_ratio) not in (int, float) or not math.isfinite(alert_ratio) or not 0 < alert_ratio <= 1:
        raise ValueError("Alert threshold must be finite and in (0, 1]")
    a_rate, b_rate = a_selected / a_total, b_selected / b_total
    ratio = b_rate / a_rate if a_rate else None
    return {
        "a_rate": a_rate, "b_rate": b_rate,
        "b_to_a_ratio": ratio,
        "b_minus_a_percentage_points": 100 * (b_rate - a_rate),
        "alert": ratio is None or ratio < alert_ratio,
        "interpretation": "Investigation signal only; not causal or legal proof"
    }


def risk_score(likelihood, impact):
    if any(type(x) is not int or not 1 <= x <= 5 for x in (likelihood, impact)):
        raise ValueError("Ordinal scores must be integers from 1 through 5")
    score = likelihood * impact
    band = "critical" if score >= 17 else "high" if score >= 10 else "moderate" if score >= 5 else "low"
    return score, band
