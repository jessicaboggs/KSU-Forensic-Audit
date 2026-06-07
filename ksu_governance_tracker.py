#!/usr/bin/env python3
import os
import json
import sys
from datetime import datetime

def run_governance_analysis():
    print("--- Initializing KSU Institutional Governance Auditor ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded structural compliance layers.\n")
        
        # Pull records out safely using dictionary .get()
        governance_log = data.get("governance_records", {})
        meeting_dates = governance_log.get("board_session_dates", [])
        voting_quorum = governance_log.get("active_quorum_count", 0)
        unauthorized_edits = governance_log.get("unapproved_policy_modifications", 0)
        
        # 1. Evaluate Quorum Requirements (Minimum 5 active board members needed)
        print(f"[!] Active Governance Voting Pool: {voting_quorum} Members Present")
        if voting_quorum < 5:
            print(f"[FLAG - HIGH RISK] Governance failure: Quorum requirement unmet. All passed resolutions void.")
            
        # 2. Track Unapproved Structural Policy Modifications
        if unauthorized_edits > 0:
            print(f"[FLAG - AUDIT FAILURE] Detected {unauthorized_edits} unapproved policy edits skipping board loops.")
            
        # 3. Analyze Cadence and Track Inter-Session Blackouts
        if len(meeting_dates) >= 2:
            # Parse the two most recent session timestamps
            fmt = "%Y-%m-%d"
            date1 = datetime.strptime(meeting_dates[-2], fmt)
            date2 = datetime.strptime(meeting_dates[-1], fmt)
            
            days_between = (date2 - date1).days
            print(f"[!] Logged Inter-Session Cadence Interval: {days_between} Days")
            
            # Statutory requirement: Board must convene bi-weekly (within 14 days)
            if days_between > 14:
                blackout_excess = days_between - 14
                print(f"[WARNING - SPOLIATION] Bi-weekly mandate breach detected: {blackout_excess} day blackout extension.")
        else:
            print("[INFO] Insufficient sequence density to evaluate cadence windows.")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    run_governance_analysis()
