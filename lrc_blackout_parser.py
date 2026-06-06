import pandas as pd
from datetime import datetime

# Programmatic mapping of the four LRC screenshots
lrc_audit_ledger = {
    "FY 2023": {"status": "Retroactive Batch Dump", "days_delayed": 429, "evidence_file": "fy2023_blackout.png"},
    "FY 2024": {"status": "Official INCOMPLETE Stamp", "days_delayed": 365, "evidence_file": "fy2024_incomplete.png"},
    "FY 2025": {"status": "2-Year Audit Presentation Lag", "days_delayed": 730, "evidence_file": "fy2025_lag.png"},
    "FY 2026": {"status": "Active 4-Month Reporting Void", "days_delayed": 125, "evidence_file": "fy2026_void.png"}
}

def compile_whistleblower_metrics():
    df = pd.DataFrame.from_dict(lrc_audit_ledger, orient='index')
    print("═══ KSU CHRONIC STATUTORY BREACH MANIFEST ═══")
    print(df[["status", "days_delayed"]])
    print(f"Total Cumulative Delinquency: {df['days_delayed'].sum()} Days of Institutional Blindness.")
    
if __name__ == "__main__":
    compile_whistleblower_metrics()
