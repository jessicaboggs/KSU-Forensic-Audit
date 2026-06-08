#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import requests

# --- Configuration & Paths ---
EVIDENCE_LOG = "data_layers/official_claims.json"
TARGET_ENDPOINTS = [
    "https://ksu.edu",
    "https://ksu.edu",
    "https://ksu.edu"
]
MAX_WORKERS = 5
TIMEOUT_SEC = 10

def check_endpoint(url):
    """Evaluates target headers to isolate 404 deletions or 302/301 redirections."""
    timestamp = datetime.utcnow().isoformat() + "Z"
    try:
        # allow_redirects=False captures the raw 301/302 footprint before the browser jumps
        response = requests.head(url, allow_redirects=False, timeout=TIMEOUT_SEC)
        status = response.status_code
        location = response.headers.get("Location", "N/A")
        
        print(f"📡 [{status}] Checked: {url}")
        
        # Track 301/302 (Routing Vectors) and 404 (Destructive Spoliation)
        if status in [301, 302, 404]:
            return {
                "timestamp": timestamp,
                "url": url,
                "status_code": status,
                "classification": "Spoliation/Routing Vector" if status in [301, 302] else "Destructive Deletion",
                "redirect_destination": location,
                "flagged": True
            }
            
    except requests.exceptions.RequestException as e:
        print(f"❌ [FAIL] Connection error on: {url}")
        return {
            "timestamp": timestamp,
            "url": url,
            "status_code": "CONNECTION_FAILURE",
            "classification": "Network Disruption / Portal Blackout",
            "error_detail": str(e),
            "flagged": True
        }
    return None

def update_evidence_ledger(anomalies):
    """Appends caught spoliation footprints to the data layer matrix."""
    if not os.path.exists(EVIDENCE_LOG):
        data = {"spoliation_tracking_ledger": []}
    else:
        with open(EVIDENCE_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {"spoliation_tracking_ledger": []}
                
    if "spoliation_tracking_ledger" not in data:
        data["spoliation_tracking_ledger"] = []
        
    data["spoliation_tracking_ledger"].extend(anomalies)
    
    with open(EVIDENCE_LOG, "w") as f:
        json.dump(data, f, indent=4)
    print(f"📂 [*] Ledger Updated. {len(anomalies)} routing vectors logged.")

def main():
    print("🚀 Initializing Automated 404/302 Fail Tracker...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(check_endpoint, TARGET_ENDPOINTS))
        
    anomalies = [r for r in results if r is not None]
    
    if anomalies:
        update_evidence_ledger(anomalies)
    else:
        print("[✓] Scan complete. Zero data layer routing anomalies detected.")

if __name__ == "__main__":
    main()
