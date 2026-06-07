#!/usr/bin/env python3
import os
import json
import sys

def run_award_verification():
    print("--- Initializing KSU Procurement & Award Level Verifier ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded institutional allocation layers.\n")
        
        # Isolate procurement logs safely
        procurement_log = data.get("procurement_records", {})
        single_source_total = procurement_log.get("single_source_award_total", 0.0)
        board_threshold_limit = procurement_log.get("statutory_board_threshold", 50000.00)
        authorization_secured = procurement_log.get("board_prior_authorization", False)
        
        print(f"[!] Logged Single-Source Contract Value : ${single_source_total:,}")
        print(f"[!] Statutory Board Clearance Ceiling    : ${board_threshold_limit:,}")
        
        # 1. Audit Procurement Thresholds & Prior Authorization Boundaries
        if single_source_total > board_threshold_limit:
            print(f"[FLAG - HIGH RISK] THRESHOLD VIOLATION: Contract exceeds the standard ceiling.")
            
            if not authorization_secured:
                print("[FLAG - AUDIT FAILURE] CRITICAL NON-COMPLIANCE: No prior Board of Regents clearance logged.")
                print("                       All outlays matching this signature violate state procurement guidelines.")
            else:
                print("[✓] Authorization Layer: Post-threshold contract backed by retroactive clearance.")
        else:
            print("[✓] Procurement Scope: Allocation sits safely within standard administrative bounds.")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    run_award_verification()
