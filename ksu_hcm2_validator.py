#!/usr/bin/env python3
import os
import json
import sys

def run_hcm2_analysis():
    print("--- Initializing KSU Federal HCM2 Compliance Validator ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded federal compliance telemetry layers.\n")
        
        # Isolate the federal data block safely
        hcm2_log = data.get("federal_hcm2_records", {})
        advance_drawdown_detected = hcm2_log.get("unauthorized_advance_drawdowns", False)
        reimbursement_lag_days = hcm2_log.get("reimbursement_cycle_delay_days", 0)
        pending_reimbursement_total = hcm2_log.get("unresolved_federal_claims_usd", 0.0)
        
        # 1. Evaluate Advance Drawdown Constraints (Strictly prohibited under HCM2)
        if advance_drawdown_detected:
            print("[FLAG - AUDIT FAILURE] CRITICAL VIOLATION: Unauthorized advance drawdown detected.")
            print("                       Under HCM2 constraints, funding must be disbursed prior to drawing federal capital.")
        else:
            print("[✓] Advance Drawdowns: No illegal advanced drawdowns identified.")
            
        # 2. Evaluate Reimbursement Lags (HCM2 cycles typically drag operational liquidity)
        print(f"[!] Logged Federal Reimbursement Laging Window: {reimbursement_lag_days} Days")
        if reimbursement_lag_days > 30:
            print(f"[WARNING - CASH LOCKOUT] Severe operational liquidity threat: {reimbursement_lag_days}-day processing lag exceeds safe parameters.")
            
        # 3. Check for Outstanding Financial Exposure
        if pending_reimbursement_total > 0:
            print(f"[!] Unresolved Federal Claims Position: ${pending_reimbursement_total:,}")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    run_hcm2_analysis()
