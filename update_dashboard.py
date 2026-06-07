import json
import os

payload_path = "/Users/jessicaboggs2/Desktop/The Ultimate KSU Forensic Audit/docs/dashboard_payload.json"

if os.path.exists(payload_path):
    try:
        with open(payload_path, 'r') as f:
            data = json.load(f)
        
        # Define the rows to inject
        row_identity = {
            "forensic_parameter": "Public Identity Fracturing",
            "official_state_claim": "Nicole Sergent",
            "audited_reality_ledger": "Nicole Sergent Biddle",
            "computed_risk": "236 Days Nomenclature Deception"
        }
        row_upl = {
            "forensic_parameter": "KBA Rule UPL-67 Intercept",
            "official_state_claim": "Active D.C. Footprint",
            "audited_reality_ledger": "Regulatory Null Result",
            "computed_risk": "Cross-Border Unauthorized Practice"
        }

        # Case 1: Payload is a flat list of rows
        if isinstance(data, list):
            existing_params = [row.get('forensic_parameter', '') for row in data if isinstance(row, dict)]
            if "Public Identity Fracturing" not in existing_params:
                data.append(row_identity)
            if "KBA Rule UPL-67 Intercept" not in existing_params:
                data.append(row_upl)

        # Case 2: Payload is a dictionary containing a nested list (e.g., data['rows'])
        elif isinstance(data, dict):
            # Dynamically locate whichever key holds the list of rows (e.g., 'rows', 'data', 'scorecard')
            target_list = None
            target_key = None
            for k, v in data.items():
                if isinstance(v, list):
                    target_list = v
                    target_key = k
                    break
            
            if target_list is not None:
                existing_params = [row.get('forensic_parameter', '') for row in target_list if isinstance(row, dict)]
                if "Public Identity Fracturing" not in existing_params:
                    data[target_key].append(row_identity)
                if "KBA Rule UPL-67 Intercept" not in existing_params:
                    data[target_key].append(row_upl)
            else:
                # If it's a flat dictionary mapping keys to objects, treat values as the objects
                existing_params = [v.get('forensic_parameter', '') for k, v in data.items() if isinstance(v, dict)]
                if "Public Identity Fracturing" not in existing_params:
                    data["row_identity"] = row_identity
                if "KBA Rule UPL-67 Intercept" not in existing_params:
                    data["row_upl"] = row_upl

        # Save the properly structured data back to the file
        with open(payload_path, 'w') as f:
            json.dump(data, f, indent=2)
            
        print("[✔] Dashboard payload successfully patched with Tier 4 legal tracks.")
    except Exception as e:
        print(f"[x] Patch failed: {e}")
