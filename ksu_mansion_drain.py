#!/usr/bin/env python3
import os
import json
import sys

def audit_mansion_and_fees():
    print("--- Initializing KSU Restricted Fee & Asset Auditor ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded 2025/2026 ledger layers.\n")
        
        # Isolate the specific real estate and fee anomalies
        historical_anomalies = data.get("legacy_2025_anomalies", {})
        diverted_activity_fees = historical_anomalies.get("student_activity_fees_swept", 0.0)
        vacant_mansion_expenditures = historical_anomalies.get("empty_mansion_maintenance_usd", 0.0)
        mansion_is_vacant = historical_anomalies.get("mansion_vacancy_status", True)
        
        # 1. Audit Student Activity Fee Diversions
        if diverted_activity_fees > 0:
            print(f"[FLAG - AUDIT FAILURE] RESTRICTED FUND RAID DETECTED!")
            print(f"                       Diverted Student Activity Fees: ${diverted_activity_fees:,}")
            print("                       Violation Vector: Unauthorized sweep of student-voted asset layers.")
            
        # 2. Audit Capital Expenditures on Empty Real Estate
        print(f"[!] Logged Presidential Mansion Outlays: ${vacant_mansion_expenditures:,}")
        if mansion_is_vacant and vacant_mansion_expenditures > 0:
            print("[FLAG - HIGH RISK] CAPITAL WASTE INDICATION: Material funds expended on a vacant asset.")
            print("                       Forensic Profile: Misallocation of capital amid active program exigency.")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    audit_mansion_and_fees()
