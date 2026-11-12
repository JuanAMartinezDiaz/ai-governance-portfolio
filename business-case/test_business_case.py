"""Checks of decision-relevant scenario arithmetic and invalid-input rejection."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("portfolio_business_case", HERE / "evaluate.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BusinessCaseTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((HERE / "assumptions.json").read_text(encoding="utf-8"))

    def results(self, data=None):
        return {item["id"]: item for item in MODULE.compare(data or self.data)}

    def test_manual_hand_calculation_includes_rework_and_exceptions(self):
        result = self.results()["manual"]
        self.assertEqual(result["assumed_rework_events_monthly"], 40)
        self.assertEqual(result["assumed_exception_events_monthly"], 60)
        self.assertEqual(result["internal_human_hours_monthly"], 221.33)
        self.assertEqual(result["recurring_economic_cost_monthly_usd"], 13280)
        self.assertEqual(result["first_year_economic_cost_usd"], 159360)

    def test_reviewer_first_ranking_does_not_claim_effort_savings(self):
        result = self.results()["reviewer_first_ranking"]
        self.assertLess(result["monthly_internal_capacity_hours_vs_manual"], 0)
        self.assertLess(result["first_year_economic_saving_vs_manual_usd"], 0)
        self.assertIsNone(result["estimated_setup_payback_operating_months"])

    def test_extraction_all_in_first_year_cost_includes_assurance_and_setup(self):
        result = self.results()["extraction_only"]
        self.assertEqual(result["upfront_economic_cost_usd"], 12600)
        self.assertEqual(result["first_year_economic_cost_usd"], 146280)
        self.assertEqual(result["first_year_economic_saving_vs_manual_usd"], 13080)
        self.assertEqual(result["first_year_internal_capacity_hours_vs_manual"], 428)

    def test_slow_extraction_review_erases_economic_case(self):
        altered = deepcopy(self.data)
        altered["options"][2]["direct_review_minutes_per_application"] = 12
        self.assertLess(self.results(altered)["extraction_only"]["first_year_economic_saving_vs_manual_usd"], 0)

    def test_extra_setup_cost_changes_year_one_not_monthly_effort(self):
        before = self.results()["extraction_only"]
        altered = deepcopy(self.data)
        altered["options"][2]["independent_assurance_cost_usd"] += 1000
        after = self.results(altered)["extraction_only"]
        self.assertEqual(after["internal_human_hours_monthly"], before["internal_human_hours_monthly"])
        self.assertEqual(after["first_year_economic_saving_vs_manual_usd"], before["first_year_economic_saving_vs_manual_usd"] - 1000)

    def test_high_volume_does_not_hide_insufficient_monthly_capacity(self):
        self.data["monthly_applications"] = 2000
        result = self.results()["extraction_only"]
        self.assertFalse(result["fits_assumed_monthly_batch_window"])
        self.assertGreater(result["estimated_batch_completion_business_days"], 20)

    def test_invalid_inputs_cannot_produce_an_economic_case(self):
        for field, value in [("monthly_applications", 0), ("reviewers_in_parallel", 0), ("monthly_applications", 2.5), ("loaded_internal_hourly_cost_usd", float("nan"))]:
            with self.subTest(field=field, value=value):
                altered = deepcopy(self.data)
                altered[field] = value
                with self.assertRaises(ValueError):
                    MODULE.compare(altered)
        altered = deepcopy(self.data)
        altered["options"][2]["exception_rate"] = 1.1
        with self.assertRaises(ValueError):
            MODULE.compare(altered)

    def test_no_scenario_can_authorize_real_execution(self):
        self.data["real_execution_authorized"] = True
        with self.assertRaises(ValueError):
            MODULE.evaluate(self.data)


if __name__ == "__main__":
    unittest.main()
