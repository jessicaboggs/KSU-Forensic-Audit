#!/usr/bin/env python3
import os
import json
import sys
def run_hcm2_audit():
    print("--- Initializing KSU HCM2 Reimbursement Compliance Engine ---")
    data_source = "january_2026_financial_core.json"

    if not os.path.exists(data_source):
        print(f"[INFO] Financial source file missing. Skipping analysis.")
        sys.exit(0)

    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        
        realities = data.get("financial_realities", {})
        notes = data.get("forensic_notes", {})
        
        hcm2_audited_count = 0
        critical_documentation_failures = 0
        
        # Pull high level indicators to evaluate HCM2 trigger limits
        restricted_swept = realities.get("restricted_funds_swept", 0)
        operating_cash = realities.get("operating_cash_balance", 0)
        
        print(f"[INFO] Evaluating financial baseline metrics against federal HCM2 guidelines...")
        
        if restricted_swept > 0:
            critical_documentation_failures += 1
            print(f"[CRITICAL FLAG - HCM2 VIOLATION] Unauthorized sweep of restricted funds detected: ${restricted_swept:,}")
            print("  -> Under federal Heightened Cash Monitoring 2 rules, restricted student aid/grant funds cannot be used to cover operational deficits.")
            
        if operating_cash < 0:
            print(f"[WARNING - ESCALATION] Deficit spending profile complicates federal reimbursement cycles.")
            
        if "spoliation_indicator" in notes:
            critical_documentation_failures += 1
            print(f"[CRITICAL FLAG - AUDITTRAIL BLOCKED] {notes['spoliation_indicator']}")
            print("  -> Failure to provide untampered systems data results in immediate suspension of standard G5 reimbursement streams.")

        print("\n--- HCM2 Evaluation Summary ---")
        print(f"Critical Compliance Failures Identified: {critical_documentation_failures}")
        if critical_documentation_failures > 0:
            print("STATUS: REIMBURSEMENT STATUS SUSPENDED / HIGH RISK FOR INJUNCTION")
        else:
            print("STATUS: NOMINAL PASS")

    except Exception as e:
        print(f"[CRITICAL] Error parsing dataset: {str(e)}")

if __name__ == '__main__':
    run_hcm2_audit()
