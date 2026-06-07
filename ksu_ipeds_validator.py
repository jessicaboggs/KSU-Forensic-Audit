#!/usr/bin/env python3
import os
import json
import sys

def run_ipeds_analysis():
    print("--- Initializing KSU Federal IPEDS Data Validator ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded federal reporting telemetry layers.\n")
        
        # Isolate the IPEDS data block safely
        ipeds_log = data.get("federal_ipeds_records", {})
        reported_enrollment = ipeds_log.get("reported_full_time_cohort", 0)
        historical_baseline = ipeds_log.get("historical_baseline_cohort", 0)
        retention_rate = ipeds_log.get("calculated_retention_percentage", 100.0)
        erasure_flag_detected = ipeds_log.get("unexplained_record_drops", False)
        
        # 1. Evaluate Cohort Variance (Check for sharp, unannounced population drop-offs)
        print(f"[!] Historical Baseline Cohort : {historical_baseline:,} Students")
        print(f"[!] Reported Enrollment Cohort : {reported_enrollment:,} Students")
        
        if historical_baseline > 0:
            variance_pct = ((historical_baseline - reported_enrollment) / historical_baseline) * 100
            if variance_pct >= 20.0:
                print(f"[FLAG - HIGH RISK] IPEDS Data Instability: Cohort contracted by {variance_pct:.2f}% relative to baseline.")
        
        # 2. Check for explicit record erasure indicators
        if erasure_flag_detected:
            print("[FLAG - AUDIT FAILURE] CRITICAL ANOMALY: Unexplained per-capita data erasure sequence triggered.")
            print("                       Federal profiles show historical data rows omitted without institutional restatements.")
            
        # 3. Track Retention Safeguards
        print(f"[!] Logged Retention Position : {retention_rate}%")
        if retention_rate < 50.0:
            print(f"[WARNING - AMENDMENT NEEDED] Institutional risk: Retention rate below federal threshold baseline.")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    run_ipeds_analysis()
