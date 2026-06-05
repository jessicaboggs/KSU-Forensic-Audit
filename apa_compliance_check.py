import os
import json
import sys

def run_compliance_check():
    print("--- Starting APA Compliance Validation ---")
    log_file = "TAB_E-8_G5_API_Payload_Logs.json"
    
    # 1. Verification: Ensure required core files exist
    if not os.path.exists(log_file):
        print(f"[CRITICAL ERROR] Target file '{log_file}' is missing! Possible data spoliation detected.")
        sys.exit(1) # Force workflow failure if files disappear
        
    try:
        with open(log_file, 'r') as f:
            logs = json.load(f)
            
        # 2. Validation: Verify payload list integrity
        if not isinstance(logs, list):
            print("[CRITICAL ERROR] Forensic logs must be structured as a JSON Array/List.")
            sys.exit(1)
            
        print(f"[SUCCESS] Target file verified. Processing {len(logs)} payload records...")
        
        # 3. Compliance Scan Loop
        violations_count = 0
        for index, record in enumerate(logs):
            # Check for critical forensic keys
            if "payload" not in record or "timestamp" not in record:
                print(f"[VIOLATION] Record index {index} is missing structural forensic telemetry.")
                violations_count += 1
                
        if violations_count > 0:
            print(f"[WARNING] Scan complete. Found {violations_count} non-compliant artifacts.")
        else:
            print("[SUCCESS] Core API dataset complies fully with forensic parameters.")
            
    except json.JSONDecodeError:
        print("[CRITICAL ERROR] Target log file is corrupted or poorly formatted JSON.")
        sys.exit(1)

if __name__ == "__main__":
    run_compliance_check()
