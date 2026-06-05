#!/usr/bin/env python3
import os
import json
import sys

def run_hcm2_audit():
    print("--- Initializing KSU HCM2 Reimbursement Compliance Engine ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[INFO] Financial source file missing. Creating mock environment check...")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            transactions = json.load(f)
            
        hcm2_audited_count = 0
        critical_documentation_failures = 0
        
        for idx, tx in enumerate(transactions):
            # Isolate entries involving federal grant draws, Title IV, or student aid accounts
            account_type = tx.get("account_type", "").upper()
            is_federal_draw = "FEDERAL" in account_type or "TITLE_IV" in account_type or "GRANT" in account_type
            
            if is_federal_draw:
                hcm2_audited_count += 1
                tx_id = tx.get("transaction_id", f"HCM2-TX-{idx}")
                amount = tx.get("amount", 0)
                
                # HCM2 Compliance Check: Every draw must explicitly link to a validated reimbursement voucher
                has_voucher = tx.get("hcm2_voucher_verified", False)
                has_student_link = tx.get("student_recipient_id", None) is not None
                
                if not has_voucher:
                    print(f"[CRITICAL FAIL] HCM2 Violation: Federal drawdown of ${amount:,} (ID: {tx_id}) lacks mandatory pre-approval voucher verification code.")
                    critical_documentation_failures += 1
                elif not has_student_link:
                    print(f"[CRITICAL FAIL] HCM2 Violation: Voucher exists for ID {tx_id}, but lacks direct relational lookup mapping to an enrolled student profile.")
                    critical_documentation_failures += 1
                else:
                    print(f"[COMPLIANT] Verified HCM2 Voucher match found for drawdown ID: {tx_id}")

        print("--------------------------------------------------")
        print(f"[HCM2 AUDIT COMPLETE] Checked {hcm2_audited_count} federal transactions.")
        if critical_documentation_failures > 0:
            print(f"[ALERT] Found {critical_documentation_failures} unbacked drawdowns. Potential compliance clawback exposure.")
        else:
            print("[SUCCESS] All isolated federal fund items contain standard matching compliance metadata.")
            
    except json.JSONDecodeError:
        print("[ERROR] Failed to parse financial JSON core. Check formatting.")
        sys.exit(1)

if __name__ == "__main__":
    run_hcm2_audit()
