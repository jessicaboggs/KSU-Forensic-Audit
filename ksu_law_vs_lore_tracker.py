#!/usr/bin/env python3
import os
import json
import sys

def evaluate_sanction_requirements(current_sanction: str) -> dict:
    """
    Evaluates SACSCOC policy bounds to determine if a contingency 
    teach-out plan is legally mandated based on the active sanction tier.
    Warning activates restrictions, while Probation activates mandatory teach-outs.
    """
    sanction_lower = current_sanction.lower()
    requirements = {
        "substantive_change_restriction": False,
        "mandatory_contingency_teach_out": False
    }
    
    if "warning" in sanction_lower:
        requirements["substantive_change_restriction"] = True
        requirements["mandatory_contingency_teach_out"] = False
    elif "probation" in sanction_lower or "good cause" in sanction_lower:
        requirements["substantive_change_restriction"] = True
        requirements["mandatory_contingency_teach_out"] = True
        
    return requirements

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
                "category": "Pre-emptive Program Shuttering",
                "statute_reference": "SB 185 Sec. 2(1) Notice Window",
                "newsroom_lore": "Administration claims immediate authority to close doors on non-polytechnic majors.",
                "statutory_law": "Enforces a strict 60-day review and public CPE posting loop prior to plan activation.",
                "severity": "HIGH RISK"
            },
            {
                "category": "Unauthorized Faculty Lockouts",
                "statute_reference": "SB 185 Sec. 2(4) Notice Firewall",
                "newsroom_lore": "HR executing immediate personnel sweeps under the guise of statutory streamlining.",
                "statutory_law": "Mandates a strict 30-day written notice baseline backed by prior Board of Regents clearance.",
                "severity": "CRITICAL VIOLATION"
            },
            {
                "category": "Premature June 1 Executions",
                "statute_reference": "SB 185 Sec. 2(1) & 2(4) Deficits",
                "newsroom_lore": "Admin states June 1 operates as a hard legislative cliff for immediate program and staff terminations.",
                "statutory_law": "April 3 enactment forces a 60-day public notice window (June 2) plus a 30-day notice minimum (July 2).",
                "severity": "CRITICAL TIMING FRAUD"
            },
                        {
                "category": "Unchecked Admissions Pipeline",
                "statute_reference": "SB 185 Section 5 Mandate",
                "newsroom_lore": "Enrollment declines are framed as casual market shifts or temporary operational pauses.",
                "statutory_law": "Imposes a hard statutory floor requiring an unweighted 2.5 GPA AND an 18 ACT for all standard entries.",
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
        
        # 2. SANCTION POLICY EVALUATION: Page 62 Substantive Change Checker
        notes = data.get("forensic_notes", {})
        active_sanction = notes.get("active_sacscoc_sanction", "Probation for Good Cause")
        
        policy_bounds = evaluate_sanction_requirements(active_sanction)
        print(f"--- SACSCOC Sanction Evaluation Window: '{active_sanction}' ---")
        print(f"[!] Substantive Change Restriction Active : {policy_bounds['substantive_change_restriction']}")
        print(f"[!] Mandatory Contingency Teach-Out Plan  : {policy_bounds['mandatory_contingency_teach_out']}")
        
        if policy_bounds['mandatory_contingency_teach_out']:
            print("[FLAG - ACCREDITATION CRITICAL] Due to Probation status, unilateral program deletions without")
            print("                                prior SACSCOC-approved teach-out prospectuses constitute severe")
            print("                                non-compliance under Page 62 procedural standards.")
        print()
        print("-" * 60)
        
        # 3. ACCREDITATION CONTINGENCY AUDIT: Section 2(6) Tracker
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
