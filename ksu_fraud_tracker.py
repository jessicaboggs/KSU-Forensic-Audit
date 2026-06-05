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
            transactions = json.load(f)
            
        print(f"[INFO] Successfully loaded {len(transactions)} transaction items for auditing...")
        
        anomalies_detected = 0
        seen_transactions = {} # Memory hash map to check for velocity/duplicate spacing

        for idx, tx in enumerate(transactions):
            if isinstance(tx, str):
                tx = json.loads(tx)
                
            amount = tx.get("amount", 0)
            vendor = tx.get("vendor", "UNKNOWN VENDOR")
            timestamp_str = tx.get("timestamp", "")
            tx_id = tx.get("transaction_id", f"GEN-ID-{idx}")


            
            # 1. Flag Large Rounded Sums (Common indicator of missing invoices/shell transfers)
            if amount >= 5000 and amount % 1000 == 0:
                print(f"[FLAG - ROUNDED AMOUNT] High-value round sum: ${amount:,} to {vendor} (ID: {tx_id})")
                anomalies_detected += 1
                
            # 2. Flag Off-Hours Activity (System updates or ledger overrides during dead hours)
            if timestamp_str:
                try:
                    # Expecting typical ISO timestamp standard (YYYY-MM-DDTHH:MM:SS)
                    tx_time = datetime.fromisoformat(timestamp_str.replace("Z", ""))
                    if tx_time.hour >= 22 or tx_time.hour <= 4:
                        print(f"[FLAG - TIMING ANOMALY] Suspicious processing hour ({tx_time.strftime('%H:%M:%S')}) for transaction {tx_id}")
                        anomalies_detected += 1
                except ValueError:
                    pass # Skip timestamp formatting anomalies here; handle in structural checks
                    
            # 3. Duplicate Transaction Cascades (Splitting invoices into identical pieces to bypass approval ceilings)
            tx_signature = f"{vendor}_{amount}"
            if tx_signature in seen_transactions:
                print(f"[FLAG - SPLIT MATCH] Warning: Duplicate billing velocity pattern matching vendor '{vendor}' for amount ${amount:,}")
                anomalies_detected += 1
            else:
                seen_transactions[tx_signature] = timestamp_str

        print("--------------------------------------------------")
        print(f"[SCAN COMPLETE] Total anomalous profiles surfaced: {anomalies_detected}")
        
    except json.JSONDecodeError:
        print("[CRITICAL] Financial core dataset corrupted or unreadable. Analysis halted.")
        sys.exit(1)

if __name__ == "__main__":
    run_fraud_analysis()

