#!/usr/bin/env python3
"""Deterministic scenario arithmetic; no model, applicants or external services."""

import argparse
from copy import deepcopy
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent


def number(value, name):
    if isinstance(value, bool):
        raise ValueError(f"{name} must be numeric")
    try:
        result = Decimal(str(value))
    except Exception as exc:
        raise ValueError(f"{name} must be numeric") from exc
    if not result.is_finite() or result < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return result


def rounded(value, places=2):
    return float(value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP))


def validate(data):
    if data.get("real_execution_authorized") is not False:
        raise ValueError("This scenario cannot authorize real execution")
    positive = (
        "monthly_applications", "months", "loaded_internal_hourly_cost_usd",
        "reviewers_in_parallel", "hours_per_business_day", "workdays_per_month",
    )
    for field in positive:
        if number(data[field], field) <= 0:
            raise ValueError(f"{field} must be positive")
    for field in ("monthly_applications", "months", "reviewers_in_parallel", "workdays_per_month"):
        if number(data[field], field) % 1:
            raise ValueError(f"{field} must be an integer")
    if number(data["months"], "months") != 12:
        raise ValueError("The first-year comparison requires a 12-month horizon")
    number(data["queue_wait_business_hours"], "queue_wait_business_hours")
    ids = [option["id"] for option in data["options"]]
    if len(ids) != len(set(ids)) or set(ids) != {"manual", "reviewer_first_ranking", "extraction_only"}:
        raise ValueError("Exactly one of each declared alternative is required")
    fields = (
        "direct_review_minutes_per_application", "correctable_rework_rate",
        "minutes_per_rework_event", "exception_rate", "minutes_per_exception",
        "monthly_governance_hours", "batch_compute_business_hours",
        "monthly_platform_cost_usd", "setup_internal_hours", "setup_vendor_cost_usd",
        "independent_assurance_cost_usd",
    )
    for option in data["options"]:
        for field in fields:
            value = number(option[field], f"{option['id']}.{field}")
            if field.endswith("_rate") and value > 1:
                raise ValueError(f"{field} must be between zero and one")


def raw_metrics(data, option):
    n = number(data["monthly_applications"], "monthly_applications")
    months = number(data["months"], "months")
    hourly = number(data["loaded_internal_hourly_cost_usd"], "hourly_cost")
    d = {key: number(value, key) for key, value in option.items()
         if key not in ("id", "name", "decision_status")}
    rework = n * d["correctable_rework_rate"]
    exceptions = n * d["exception_rate"]
    direct_hours = n * d["direct_review_minutes_per_application"] / 60
    rework_hours = rework * d["minutes_per_rework_event"] / 60
    exception_hours = exceptions * d["minutes_per_exception"] / 60
    casework_hours = direct_hours + rework_hours + exception_hours
    human_hours = casework_hours + d["monthly_governance_hours"]
    labor_cost = human_hours * hourly
    recurring_cost = labor_cost + d["monthly_platform_cost_usd"]
    setup_cost = (d["setup_internal_hours"] * hourly + d["setup_vendor_cost_usd"]
                  + d["independent_assurance_cost_usd"])
    critical_path = (number(data["queue_wait_business_hours"], "queue_wait")
                     + d["batch_compute_business_hours"]
                     + casework_hours / number(data["reviewers_in_parallel"], "reviewers"))
    available_review_hours = (number(data["reviewers_in_parallel"], "reviewers")
                              * number(data["hours_per_business_day"], "hours_per_day")
                              * number(data["workdays_per_month"], "workdays"))
    return {
        "assumed_rework_events_monthly": rework,
        "assumed_exception_events_monthly": exceptions,
        "direct_review_hours_monthly": direct_hours,
        "rework_hours_monthly": rework_hours,
        "exception_hours_monthly": exception_hours,
        "casework_hours_monthly": casework_hours,
        "governance_hours_monthly": d["monthly_governance_hours"],
        "internal_human_hours_monthly": human_hours,
        "internal_human_hours_first_year_including_setup": human_hours * months + d["setup_internal_hours"],
        "internal_labor_cost_monthly_usd": labor_cost,
        "platform_cost_monthly_usd": d["monthly_platform_cost_usd"],
        "recurring_economic_cost_monthly_usd": recurring_cost,
        "upfront_economic_cost_usd": setup_cost,
        "first_year_economic_cost_usd": recurring_cost * months + setup_cost,
        "external_cash_cost_first_year_usd": d["monthly_platform_cost_usd"] * months + d["setup_vendor_cost_usd"] + d["independent_assurance_cost_usd"],
        "recurring_cost_per_application_usd": recurring_cost / n,
        "first_year_cost_per_application_usd": (recurring_cost * months + setup_cost) / (n * months),
        "estimated_batch_completion_business_days": critical_path / number(data["hours_per_business_day"], "day"),
        "reviewer_casework_utilization_ratio": casework_hours / available_review_hours,
    }


def compare(data):
    validate(data)
    raw = {item["id"]: raw_metrics(data, item) for item in data["options"]}
    base = raw["manual"]
    results = []
    for item in data["options"]:
        metrics = raw[item["id"]]
        saving = base["recurring_economic_cost_monthly_usd"] - metrics["recurring_economic_cost_monthly_usd"]
        incremental_setup = metrics["upfront_economic_cost_usd"] - base["upfront_economic_cost_usd"]
        record = {"id": item["id"], "name": item["name"], "decision_status": item["decision_status"]}
        record.update({key: rounded(value, 6 if "ratio" in key else 2) for key, value in metrics.items()})
        record.update({
            "monthly_internal_capacity_hours_vs_manual": rounded(base["internal_human_hours_monthly"] - metrics["internal_human_hours_monthly"]),
            "first_year_internal_capacity_hours_vs_manual": rounded(base["internal_human_hours_first_year_including_setup"] - metrics["internal_human_hours_first_year_including_setup"]),
            "monthly_economic_saving_vs_manual_usd": rounded(saving),
            "first_year_economic_saving_vs_manual_usd": rounded(base["first_year_economic_cost_usd"] - metrics["first_year_economic_cost_usd"]),
            "estimated_setup_payback_operating_months": rounded(incremental_setup / saving) if saving > 0 and incremental_setup > 0 else None,
            "fits_assumed_monthly_batch_window": metrics["estimated_batch_completion_business_days"] <= number(data["workdays_per_month"], "workdays") and metrics["reviewer_casework_utilization_ratio"] <= 1,
        })
        results.append(record)
    return results


def evaluate(data):
    results = compare(data)
    sensitivity = []
    for axis in data.get("sensitivity", []):
        for value in axis["values"]:
            altered = deepcopy(data)
            if axis["scope"] == "global":
                altered[axis["field"]] = value
            elif axis["scope"] == "extraction_only":
                option = next(item for item in altered["options"] if item["id"] == "extraction_only")
                option[axis["field"]] = value
            else:
                raise ValueError("Unsupported sensitivity scope")
            result = next(item for item in compare(altered) if item["id"] == "extraction_only")
            sensitivity.append({
                "scope": axis["scope"], "field": axis["field"], "input_value": value,
                "first_year_economic_saving_vs_manual_usd": result["first_year_economic_saving_vs_manual_usd"],
                "monthly_internal_capacity_hours_vs_manual": result["monthly_internal_capacity_hours_vs_manual"],
                "estimated_batch_completion_business_days": result["estimated_batch_completion_business_days"],
                "fits_assumed_monthly_batch_window": result["fits_assumed_monthly_batch_window"],
            })
    altered = deepcopy(data)
    extraction = next(item for item in altered["options"] if item["id"] == "extraction_only")
    original_minutes = number(extraction["direct_review_minutes_per_application"], "review_minutes")
    extraction["direct_review_minutes_per_application"] = 0
    zero = {item["id"]: raw_metrics(altered, item) for item in altered["options"]}
    cost_per_minute = (number(data["monthly_applications"], "volume") / 60
                       * number(data["loaded_internal_hourly_cost_usd"], "hourly")
                       * number(data["months"], "months"))
    break_even = (zero["manual"]["first_year_economic_cost_usd"]
                  - zero["extraction_only"]["first_year_economic_cost_usd"]) / cost_per_minute
    return {
        "case_id": data["case_id"], "prepared": data["prepared"],
        "evidence_status": "calculated_from_assumed_inputs_not_observed_or_model_tested",
        "real_execution_authorized": False,
        "method": "deterministic_arithmetic_no_random_simulation_no_external_calls",
        "alternatives": results,
        "extraction_first_year_break_even_direct_review_minutes": rounded(break_even),
        "extraction_assumed_direct_review_minutes": rounded(original_minutes),
        "sensitivity_method": "one_input_at_a_time_all_other_base_assumptions_fixed_no_probabilities",
        "sensitivity": sensitivity,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare calculated output with committed results.json")
    parser.add_argument("--write", action="store_true", help="regenerate results.json")
    args = parser.parse_args()
    if args.check and args.write:
        parser.error("Choose --check or --write")
    data = json.loads((HERE / "assumptions.json").read_text(encoding="utf-8"))
    output = evaluate(data)
    text = json.dumps(output, indent=2, ensure_ascii=False) + "\n"
    target = HERE / "results.json"
    if args.check:
        if not target.exists() or json.loads(target.read_text(encoding="utf-8")) != output:
            print("FAIL: business-case/results.json differs from calculated scenario output", file=sys.stderr)
            return 1
        print("PASS: business-case/results.json matches deterministic scenario calculations")
    elif args.write:
        target.write_text(text, encoding="utf-8")
        print("Wrote business-case/results.json (assumed scenario; no live result)")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
