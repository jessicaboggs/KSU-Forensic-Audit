import os
import json
import hashlib
import requests
from datetime import datetime
from bs4 import BeautifulSoup

URL = "https://kysu.edu"
DATA_PATH = "data_layers/official_claims.json"

def fetch_and_track():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Isolate the main article text
    article_text = soup.find('main').get_text(strip=True) if soup.find('main') else soup.get_text()
    
    # FIX: Generates a persistent, deterministic SHA-256 hash string
    text_encoded = article_text.encode('utf-8')
    stable_hash = hashlib.sha256(text_encoded).hexdigest()
    
    # FIX: Generates the true current runtime timestamp in UTC ISO format
    current_time_iso = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    current_payload = {
        "url": URL,
        "last_checked": current_time_iso,
        "claims": {
            "total_funding_narrative": 170000000,
            "asset_preservation": 60000000,
            "online_programs": 20000000
        },
        "raw_text_hash": stable_hash
    }
    
    # If the file already exists, check for text alterations (Spoliation)
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as f:
            old_data = json.load(f)
        if old_data.get("raw_text_hash") != current_payload["raw_text_hash"]:
            print("⚠️ ALERT: Stealth text modification detected on the official KSU Newsroom page!")
            # Trigger alert mechanisms here
            
    # Automatically ensure the data_layers directory exists before writing
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    
    with open(DATA_PATH, 'w') as f:
        json.dump(current_payload, f, indent=2)

if __name__ == "__main__":
    fetch_and_track()
