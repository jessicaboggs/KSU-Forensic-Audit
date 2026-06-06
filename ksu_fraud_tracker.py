#!/usr/bin/env python3
import os
import json
import sys
from datetime import datetime

def run_fraud_analysis():
    print("--- Initializing KSU Financial Fraud Tracker Engine ---")
    data_source = "january_2026_financial_core.json"

    if not os.path.exists(data_source):
        print(f"[ERROR] Financial data file '{data_source}' not found. Skipping analysis loop.")
        sys.exit(0)

    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded financial core data summary.")

        realities = data.get("financial_realities", {})
        notes = data.get("forensic_notes", {})

        # 1. Check for swept or diverted funds
        restricted_swept = realities.get("restricted_funds_swept", 0)
        if restricted_swept > 0:
            print(f"[FLAG - HIGH RISK] Restricted funds diverted/swept: ${restricted_swept:,}")

        # 2. Check for negative cash flow metrics
        operating_cash = realities.get("operating_cash_balance", 0)
        # Target the accelerated liquidity collapse threshold
        print(f"[!] Operating Cash Posture: {operating_cash} Days Cash on Hand.")
        if operating_cash <= -30:
            print(" [CRITICAL] BREACH DETECTED: Liquidity is over negative 30 days.")
            print(" [VIOLATION] SACSCOC Good-Cause Forfeiture Threshold Achieved.")
            print(" [LEGAL STATUS]: TERMINAL FINANCIAL INSOLVENCY ENFORCED.")

        # 3. Check for unreconciled/void anomalies
        unreconciled_void = realities.get("unreconciled_student_void", 0)
        if unreconciled_void > 0:
            print(f"[FLAG - AUDIT FAILURE] Unreconciled student voids: ${unreconciled_void:,}")

        # 4. Check for compliance/spoliation warnings
        if "apa_violation_trigger" in notes:
            print(f"[WARNING - APA] {notes['apa_violation_trigger']}")
        if "spoliation_indicator" in notes:
            print(f"[WARNING - SPOLIATION] {notes['spoliation_indicator']}")
    except Exception as e:
        print(f"[CRITICAL] Error parsing dataset: {str(e)}")

if __name__ == '__main__':
    run_fraud_analysis()



