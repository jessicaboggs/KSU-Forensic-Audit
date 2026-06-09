import concurrent.futures
import requests
import json
import os
from datetime import datetime

# Absolute repo path constraints
BASE_DIR = "/Users/jessicaboggs2/Desktop/The Ultimate KSU Forensic Audit"
EVIDENCE_LEDGER_PATH = os.path.join(BASE_DIR, "docs", "routing_anomalies.json")

# Target KSU subdirectories executing the 2026 Shell Game blackouts
TARGET_ENDPOINTS = {
    "Faculty_Senate_Minutes": "https://kysu.edu",
    "Digital_Catalog_Archive": "https://kysu.edu",
    "Academic_Referral_Report": "https://kysu.edu",
    "Board_Meeting_Dockets": "https://kysu.edu"
}

MAX_WORKERS = 4
REQUEST_TIMEOUT = 5

def check_endpoint(name, url):
    """Executes a live network probe to catch hard-coded 404/302 data redirects."""
    try:
        # Pass a standard browser header to bypass standard proxy-bounce barriers
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT, allow_redirects=False)
        
        # Flag any abnormal routing signature returning a block or unexpected redirect
        if response.status_code in [404, 302, 301]:
            return {
                "endpoint": name,
                "target_url": url,
                "http_status": response.status_code,
                "detected_at": datetime.now().isoformat(),
                "anomaly_type": "HARD_404_BLOCK" if response.status_code == 404 else "PROXIED_302_REDIRECT"
            }
    except requests.exceptions.RequestException as e:
        return {
            "endpoint": name,
            "target_url": url,
            "http_status": "TIMEOUT/EXCEPTION",
            "detected_at": datetime.now().isoformat(),
            "anomaly_type": f"CONNECTION_DROPPED: {type(e).__name__}"
        }
    return None

def update_evidence_ledger(anomalies):
    """Programmatically writes detected network spoliation events straight to the docs layer."""
    os.makedirs(os.path.dirname(EVIDENCE_LEDGER_PATH), exist_ok=True)
    
    # Maintain continuous logs across runs
    if os.path.exists(EVIDENCE_LEDGER_PATH):
        try:
            with open(EVIDENCE_LEDGER_PATH, 'r', encoding='utf-8') as f:
                current_log = json.load(f)
        except json.JSONDecodeError:
            current_log = []
    else:
        current_log = []
        
    current_log.extend(anomalies)
    
    with open(EVIDENCE_LEDGER_PATH, 'w', encoding='utf-8') as f:
        json.dump(current_log, f, indent=4)
    print(f"📁 Evidence ledger synchronized. {len(anomalies)} anomalies logged to: {EVIDENCE_LEDGER_PATH}")

def main():
    print("🛰️ Initializing Automated 404/302 Fail Tracker...")
    anomalies = []
    
    # Fire off concurrent network threads to execute the trace simultaneously
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(check_endpoint, name, url): name for name, url in TARGET_ENDPOINTS.items()}
        for future in concurrent.futures.as_completed(future_to_url):
            result = future.result()
            if result:
                anomalies.append(result)
                print(f"⚠️ ANOMALY DETECTED -> [{result['endpoint']}] returned {result['http_status']}")
                
    if anomalies:
        update_evidence_ledger(anomalies)
    else:
        print("[✓] Scan complete. Zero data layer routing anomalies detected.")

if __name__ == "__main__":
    main()
