#!/usr/bin/env python3
import os
import json
import sys

def verify_foundation_filings():
    print("--- Initializing KSU Foundation Omission Detector ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded foundation record telemetry.\n")
        
        foundation_registry = data.get("foundation_filing_status", {})
        
        # Track the 2025 target filing window
        is_filed_2025 = foundation_registry.get("form_990_filed_2025", False)
        days_overdue = foundation_registry.get("filing_delay_days", 0)
        
        print(f"[!] 2025 Form 990 Filing State : " + ("FILED" if is_filed_2025 else "MISSING / OMITTED"))
        
        # 1. Flag absolute filing omissions
        if not is_filed_2025:
            print("[FLAG - HIGH RISK] TRANSPARENCY VOID: KSU Foundation, Inc. failed to submit Form 990 for 2025.")
            print(f"                       Filing Window Deficit: {days_overdue} Days Past Statutory Deadline")
            print("                       Forensic Profile     : Component segregation layer unverified.")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    verify_foundation_filings()
