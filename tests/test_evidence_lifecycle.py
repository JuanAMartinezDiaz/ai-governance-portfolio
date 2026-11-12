import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from control_lifecycle import (load_fixture, run_lifecycle, retest, strict_validate,
                               simulated_approval, approval_context, check_approval,
                               revoke_approval)
from governance import validate_inventory, classify_with_trace, REVIEW
from verify_evidence import assert_narrative_consistency, expected_artifacts


class InventoryEvidenceTests(unittest.TestCase):
    def test_accountability_fields_and_unique_ids_are_required(self):
        rows = json.loads((ROOT / "project-01-ai-system-inventory/inventory.json").read_text())
        self.assertEqual(validate_inventory(rows), rows)
        for field in ("owner", "authority", "review_trigger"):
            modified = copy.deepcopy(rows)
            del modified[0][field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_inventory(modified)
        with self.assertRaises(ValueError):
            validate_inventory(rows + [rows[0]])

    def test_string_flags_are_not_accepted_as_attested_facts(self):
        rows = json.loads((ROOT / "project-01-ai-system-inventory/inventory.json").read_text())
        rows[0]["eu_scope"] = "true"
        with self.assertRaises(ValueError):
            validate_inventory(rows)

    def test_unresolved_decision_identifies_needed_evidence(self):
        result = classify_with_trace({"eu_scope": True, "purpose_code": "unknown"})
        self.assertEqual(result["decision"], REVIEW)
        self.assertEqual(result["rule_id"], "UNKNOWN-001")
        self.assertTrue(result["required_evidence"])

    def test_structured_inputs_agree_with_narrative_arithmetic(self):
        assert_narrative_consistency()


class ControlLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.fixture = load_fixture()

    def test_baseline_exposes_failure_and_remediation_resolves_fixture(self):
        report = run_lifecycle(self.fixture)
        expected_unsafe = sum(c["expected"] == "REJECT" for c in self.fixture["cases"])
        self.assertEqual(report["baseline"]["unsafe_outputs_accepted"], expected_unsafe)
        self.assertGreater(expected_unsafe, 0)
        self.assertTrue(report["retest"]["all_expectations_met"])
        self.assertEqual(report["retest"]["unsafe_accepted"], 0)
        self.assertEqual(report["retest"]["clean_rejected"], 0)
        self.assertEqual(report["governed_rerun_checks"]["same_context"]["decision"], "ACCEPT")
        for change in ("changed_version", "changed_scope", "after_revocation"):
            self.assertEqual(report["governed_rerun_checks"][change]["decision"], "BLOCKED_REVIEW_REQUIRED")
        for result in report["retest"]["cases"]:
            with self.subTest(case=result["case_id"]):
                self.assertEqual(result["decision"], result["expected"])

    def test_missing_required_facts_and_type_substitution_are_rejected(self):
        case = self.fixture["cases"][0]
        output = copy.deepcopy(case["proposed_output"])
        del output["extracted_facts"]["education"]
        self.assertEqual(strict_validate(output, case["request"], self.fixture)["decision"], "REJECT")
        output = copy.deepcopy(case["proposed_output"])
        output["extracted_facts"]["years_experience"] = "5"
        self.assertEqual(strict_validate(output, case["request"], self.fixture)["decision"], "REJECT")

    def test_failed_retest_holds_instead_of_granting_approval(self):
        self.fixture["cases"][0]["proposed_output"]["rank"] = 1
        results = retest(self.fixture)
        decision = simulated_approval(results, approval_context(self.fixture))
        self.assertEqual(decision["status"], "SIMULATED_HOLD")
        self.assertFalse(decision["human_approval_obtained"])
        self.assertFalse(decision["production_release_authorized"])

    def test_scope_version_and_same_version_evidence_changes_invalidate(self):
        context = approval_context(self.fixture)
        approval = simulated_approval(retest(self.fixture), context)
        self.assertTrue(check_approval(approval, context)["valid"])
        for key, value in (("scope", "rank_candidates"), ("system_version", "2.0"),
                           ("contract_version", "unreviewed-contract")):
            with self.subTest(change=key):
                self.assertFalse(check_approval(approval, {**context, key: value})["valid"])
        changed = copy.deepcopy(self.fixture)
        changed["trusted_records"]["SYN-R-001"]["facts"]["years_experience"] = 6
        self.assertFalse(check_approval(approval, approval_context(changed))["valid"])

    def test_revocation_stays_effective_even_with_original_context(self):
        context = approval_context(self.fixture)
        approval = simulated_approval(retest(self.fixture), context)
        revoked = revoke_approval(approval, "Fixture change review")
        self.assertFalse(check_approval(revoked, context)["valid"])

    def test_generation_is_deterministic_and_has_explicit_limits(self):
        self.assertEqual(expected_artifacts(), expected_artifacts())
        report = run_lifecycle(self.fixture)
        self.assertIn("not_a_person", report["limited_approval"]["decision_maker"])
        self.assertGreater(len(report["limits"]), 0)


if __name__ == "__main__":
    unittest.main()
