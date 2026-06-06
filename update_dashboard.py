import os
import json
from datetime import datetime

# Setup absolute directory path mapping targets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PAYLOAD_PATH = os.path.join(DOCS_DIR, "dashboard_payload.json")

def build_dashboard_payload():
    # Construct unified system tracking dictionary payload matrix
    payload = {
        "system_status": {
            "last_updated": "2026-06-06T17:40:16Z",
            "transparency_gap_months": 18,
            "active_exigency_status": True
        },
        "public_metrics": {
            "total_emergency_bailout": 23000000.0,
            "reported_vs_actual_deficit_2021": {
                "reported": -2700000.0,
                "actual_carried_forward": -15000000.0
            },
            "unsupported_procard_spending_annual": 1300000.0,
            "polytechnic_transition": {
                "target_degree_sectors": "10",
                "minimum_gpa_requirement": "2.5"
            },
            "compliance_tracking": {
                "fy_2025_audit": {
                    "statutory_deadline": "2025-12-31",
                    "days_overdue": 157,
                    "status": "NON-EXISTENT",
                    "infraction_type": "Attestation Delay"
                }
            },
            "governance_metrics": {
                "student_government_association": {
                    "published_agendas_current_cycle": 0,
                    "minutes_availability_rate": 0.0,
                    "oversight_status": "CRITICAL_VOID"
                }
            }
        },
        "analyst_compliance_flags": {
            "cpe_independent_spend_limit": True,
            "active_hcm2_monitoring": True,
            "flagged_anomalies_count": 0
        },
        "sb_185_legal_layer": {
            "statute": "Kentucky Senate Bill 185",
            "enactment_date": "2026-04-01",
            "legal_status": "Active (Challenged in Federal Court)",
            "governance_phase": "Five-Year Polytechnic Transition",
            "monitored_metrics": {
                "financial_exigency_active": True,
                "max_independent_spend_cap": 20000.00,
                "max_academic_degree_sectors": 10,
                "minimum_freshman_gpa": 2.5,
                "minimum_freshman_act": 18
            },
            "active_litigation": {
                "plaintiffs": "KSU Students and Alumni Class Action",
                "filing_date": "2026-05-11",
                "court": "U.S. District Court for the Eastern District of Kentucky",
                "core_claim": "Violation of Title VI of the Civil Rights Act"
            }
        },
        "historical_trends": [
            {
                "fiscal_year": "2005-2010 (Baseline)",
                "ipeds_enrollment_avg": 2850,
                "institutional_deficit": 0.0,
                "audit_status": "Compliant"
            },
            {
                "fiscal_year": "2015-2020 (Pre-Exigency)",
                "ipeds_enrollment_avg": 2200,
                "institutional_deficit": -4500000.0,
                "audit_status": "Delayed"
            },
            {
                "fiscal_year": "2021-2024 (Forensic Horizon)",
                "ipeds_enrollment_avg": 1700,
                "institutional_deficit": -15000000.0,
                "audit_status": "Adverse Opinion"
            },
            {
                "fiscal_year": "2025-2026 (Current Void)",
                "ipeds_enrollment_avg": 1450,
                "institutional_deficit": None,
                "audit_status": "Missing/Overdue"
            }
        ],
        "evidentiary_index": [
            {
                "document_id": "REF-2021-AUD",
                "category": "Financial Audit",
                "title": "2021 Forensic Carried Forward Variance Analysis",
                "coverage_period": "FY 2021",
                "file_target": "EVIDENTIARY_INDEX.md",
                "verification": "Auditor Verified"
            },
            {
                "document_id": "REF-IPEDS-TREND",
                "category": "IPEDS Summary",
                "title": "Historical Enrollment & Operational Cost Core Dataset",
                "coverage_period": "2005 - 2025",
                "file_target": "ipeds_federal_comparisons.json",
                "verification": "NCES Database"
            },
            {
                "document_id": "REF-SB185-COMP",
                "category": "Legislative Mandate",
                "title": "Senate Bill 185 Polytechnic Compliance Tracking Log",
                "coverage_period": "2026 - Horizon",
                "file_target": "sb_185_compliance.json",
                "verification": "Statutory Directive"
            }
        ],
        "media_timeline": [
            {
                "date": "2023-03-23",
                "headline": "Ky. auditor refers KSU findings to prosecutors",
                "source": "Courier-Journal",
                "proquest_id": "2789593663",
                "summary": "Auditor Harmon referred files detailing a 'chaotic' budget process and $4M in unbacked ProCard spending to federal and state prosecutors."
            },
            {
                "date": "2026-04-07",
                "headline": "60 bills sent to Beshear to sign",
                "source": "Courier-Journal",
                "proquest_id": "SB185_Passage",
                "summary": "Kentucky lawmakers pass SB 185, overhauling KSU and mandating its transition into a polytechnic university."
            }
        ]
    }

    # Atomically compile and dump payload matrix back to local docs folder
    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(PAYLOAD_PATH, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)

    print(f"Success: {PAYLOAD_PATH} generated and fully synchronized.")

if __name__ == "__main__":
    build_dashboard_payload()
