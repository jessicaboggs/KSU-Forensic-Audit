#!/usr/bin/env python3
import os
import json
import sys

def run_law_vs_lore_analysis():
    print("--- Initializing KSU Law vs. Lore Compliance Tracker ---")
    data_source = "january_2026_financial_core.json"
    
    if not os.path.exists(data_source):
        print(f"[ERROR] Source registry '{data_source}' missing. Halting analysis.")
        sys.exit(0)
        
    try:
        with open(data_source, 'r') as f:
            data = json.load(f)
        print("[INFO] Successfully loaded legislative compliance matrix.\n")
        
        # 1. STRUCTURAL REALITY CHECK: Narrative vs. Statutory Law Data Structure
        discrepancies_flagged = [
            {
                "category": "Financial Stability",
                "statute_reference": "SB 185 (5-Year Exigency Directive)",
                "newsroom_lore": "PR frames structural restructuring under basic 'start, stop, and grow' optimization cycles.",
                "statutory_law": "Enacts a strict regulatory framework enforcing a multi-year state of financial emergency.",
                "severity": "CRITICAL"
            },
            {
                "category": "Academic Program Cuts",
                "statute_reference": "SB 185 (House Floor Amendment 11)",
                "newsroom_lore": "Newsroom claims focus on 'strengthening student access pathways' across traditional degrees.",
                "statutory_law": "Mandates a hard pivot to a polytechnic focus, capping maximum in-person study programs.",
                "severity": "HIGH RISK"
            },
            {
                "category": "Personnel Rights",
                "statute_reference": "SB 185 (Employment Authority)",
                "newsroom_lore": "Internal human resource memos focus on routine workforce reallocations.",
                "statutory_law": "Grants the president unilateral authority to terminate tenured faculty with brief notice.",
                "severity": "CRITICAL"
            },
            {
                "category": "Fiscal Oversight",
                "statute_reference": "SB 185 (CPE Expenditure Cap)",
                "newsroom_lore": "Financial releases emphasize autonomous institutional collaboration with higher education panels.",
                "statutory_law": "Strips procurement autonomy, forcing explicit CPE approval for expenditures exceeding regulatory limits.",
                "severity": "HIGH RISK"
            },
            {
                "category": "Accreditation Contingency Loophole",
                "statute_reference": "SB 185 Sec. 2(3) & 2(6)",
                "newsroom_lore": "Admin claims SB 185 mandates immediate program cuts to hit the 10-sector cap by June 1.",
                "statutory_law": "Explicitly forbids unilateral closures; forces alignment with prior SACSCOC approved teach-outs.",
                "dapip_evidence": "SACSCOC 12/07/2025 ledger registers zero program closures—only a Heightened Monitoring Probation order.",
                "severity": "CRITICAL AUDIT FAILURE"
            }
        ]
        
        print("--- Running Narrative vs. Statutory Law Cross-Examination ---")
        for item in discrepancies_flagged:
            print(f"[{item['severity']}] Focus Area: {item['category']}")
            print(f"    • Statute Reference : {item['statute_reference']}")
            print(f"    • Admin Narrative   : {item['newsroom_lore']}")
            print(f"    • Actual Law Code   : {item['statutory_law']}")
            if "dapip_evidence" in item:
                print(f"    • DAPIP Evidence    : {item['dapip_evidence']}")
            print()
            
        print("-" * 60)
        
        # 2. ACCREDITATION CONTINGENCY AUDIT: Section 2(6) Tracker
        academic_state = data.get("academic_program_tracking", {})
        current_sectors = academic_state.get("current_sector_count", 0)
        unapproved_cuts = academic_state.get("programs_severed_pre_sacscoc_signoff", 0)
        
        print(f"[!] Active Operational Sectors : {current_sectors} Sectors")
        
        if unapproved_cuts > 0:
            print(f"[FLAG - LAW VS LORE] ILLEGAL ACADEMIC TERMINATION DETECTED!")
            print(f"                     Unilateral program deletions: {unapproved_cuts}")
            print("                     Violation Vector: Violates SB 185 Section 2(6) master accreditation mandate.")
            print("                     Forensic Profile: Immediate threat to Title IV federal aid eligibility.")
        else:
            print("[✓] Statutory Alignment: No unapproved program terminations identified.")
            
    except Exception as e:
        print(f"[CRITICAL] Operational parsing exception: {str(e)}")

if __name__ == "__main__":
    run_law_vs_lore_analysis()
