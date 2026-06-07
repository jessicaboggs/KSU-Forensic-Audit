#!/usr/bin/env python3
import os
import json
import sys

def run_clash_detection():
    print("--- Initializing KSU Cross-Ledger Clash Detector ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded primary ledger data layers.\n")
        
        # Pull separate reporting statements to check for cross-file clashes
        realities = data.get("financial_realities", {})
        clash_log = data.get("reconciliation_clashes", {})
        
        primary_void_total = realities.get("unreconciled_student_void", 0.0)
        secondary_void_total = clash_log.get("secondary_statement_void_total", 0.0)
        variance_remediation_pool = clash_log.get("variance_remediation_allocated", 0.0)
        
        print(f"[!] Primary Internal Statement Voids   : ${primary_void_total:,}")
        print(f"[!] Secondary Regulatory Statement Voids: ${secondary_void_total:,}")
        
        # 1. Audit Balance Contradictions (Values across separate sheets MUST match)
        if primary_void_total != secondary_void_total:
            clash_delta = abs(primary_void_total - secondary_void_total)
            print(f"[FLAG - HIGH RISK] CROSS-LEDGER CLASH DETECTED: Statement asymmetric variance.")
            print(f"                       Unreconciled discrepancy gap: ${clash_delta:,}")
        else:
            print("[✓] Statement Reconciliation: Transaction totals perfectly aligned across data sets.")
            
        # 2. Monitor Specific Remediation Variance Limits ($850,000 baseline cap)
        print(f"[!] Logged Remediation Allocation Pool  : ${variance_remediation_pool:,}")
        if variance_remediation_pool > 850000.00:
            excess_variance = variance_remediation_pool - 850000.00
            print(f"[WARNING - AUDIT FAILURE] Remediation Cap Breach: Allocated funds exceed the $850k threshold by ${excess_variance:,}")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    run_clash_detection()
