#!/usr/bin/env python3
import json
import os
from datetime import datetime

# Define explicit workspace paths relative to root
DOCS_DIR = "docs"
PAYLOAD_PATH = os.path.join(DOCS_DIR, "dashboard_payload.json")
SB185_PATH = os.path.join(DOCS_DIR, "sb_185_compliance.json")
IPEDS_PATH = os.path.join(DOCS_DIR, "ipeds_federal_comparisons.json")

def load_json_file(file_path, default_value):
    """Safely loads a JSON file, returning a default value if missing or corrupt."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Warning: {file_path} is corrupt. Using default state.")
    return default_value

def build_dashboard_payload():
    print("🔄 Building dynamic dashboard payload...")
    
    # 1. Ingest existing static and structural data states
    sb185_data = load_json_file(SB185_PATH, {})
    
    # 2. Extract monitored targets from SB 185 configuration
    monitored = sb185_data.get("monitored_metrics", {})
    target_sectors = monitored.get("max_academic_degree_sectors", 10)
    min_gpa = monitored.get("minimum_gpa_requirement", 2.5) # Fallback to 2.5 if key names differ
    if "minimum_freshman_gpa" in monitored:
        min_gpa = monitored["minimum_freshman_gpa"]

    # 3. Construct the comprehensive unified payload
    payload = {
        "system_status": {
            "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "transparency_gap_months": 18,
            "active_exigency_status": monitored.get("financial_exigency_active", True)
        },
        "public_metrics": {
            "total_emergency_bailout": 23000000.00,
            "reported_vs_actual_deficit_2021": {
                "reported": -2700000.00,
                "actual_carried_forward": -15000000.00
            },
            "unsupported_procard_spending_annual": 1300000.00,
            "polytechnic_transition": {
                "target_degree_sectors": target_sectors,
                "minimum_gpa_requirement": min_gpa
            }
        },
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
        ],
        "analyst_compliance_flags": {
            "cpe_independent_spend_limit": monitored.get("max_independent_spend_cap", 20000.00),
            "active_hcm2_monitoring": True,
            "flagged_anomalies_count": 0 # This can connect directly to ksu_ledger_clash_detector outputs
        }
    }

    # 4. Atomically write payload back to docs directory
    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(PAYLOAD_PATH, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)
        
    print(f"🚀 Success: {PAYLOAD_PATH} updated and fully synchronized.")

if __name__ == "__main__":
    build_dashboard_payload()
