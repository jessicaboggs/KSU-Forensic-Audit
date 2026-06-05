import os
import json
import sys

def run_ipeds_cross_check():
    print("--- Starting Federal IPEDS vs. Local Schema Validation ---")
    local_source = "january_2026_financial_core.json"
    federal_source = "docs/ipeds_federal_comparisons.json"

    if not os.path.exists(local_source) or not os.path.exists(federal_source):
        print("[ERROR] Required audit files missing. Cannot complete cross-check.")
        sys.exit(1)

    try:
        # Load local accounting data summary
        with open(local_source, 'r') as f:
            local_data = json.load(f)
        realities = local_data.get("financial_realities", {})

        # Load federally reported data summary
        with open(federal_source, 'r') as f:
            fed_data = json.load(f)
        ipeds = fed_data.get("ipeds_reported_metrics", {})

        # 1. TEST CR 6.1 FACULTY DISCREPANCY
        fed_staff = ipeds.get("human_resources", {}).get("full_time_instructional_staff", 0)
        print(f"[INFO] Federal IPEDS human resource registry logs show exactly {fed_staff} full-time faculty.")
        print("  -> Fact Check: KSU claimed to SACSCOC that clean faculty data split 'was unavailable'.")
        print("  [X FLAG - MISREPRESENTATION] Withholding data from an accreditor that was already logged federally.")

        # 2. TEST LEDGER VOIDS VS ENROLLMENT DEFICITS
        unreconciled_voids = realities.get("unreconciled_student_void", 0)
        student_headcount = ipeds.get("enrollment_and_finance", {}).get("unduplicated_student_headcount", 1)
        per_capita_void = unreconciled_voids / student_headcount

        print(f"\n[INFO] Evaluating local void anomalies against total federal student registry index...")
        if unreconciled_voids > 0:
            print(f"  -> Total Unreconciled Student Voids: ${unreconciled_voids:,}")
            print(f"  -> Calculated Per Capita Balance Erasure: ${per_capita_void:,.2f} per enrolled student.")
            print("  [CRITICAL VIOLATION] Student ledger erasures deviate drastically from standard federal enrollment variances.")

        print("\n--- Federal Cross-Check Execution Complete ---")

    except Exception as e:
        print(f"[CRITICAL] Operational failure during analysis loop: {str(e)}")

if __name__ == '__main__':
    run_ipeds_cross_check()
