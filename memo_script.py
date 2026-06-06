import subprocess
import os

# Define file details
file_name = "Master_Memo_Dossier_Final.md"
commit_message = "Compliance: Establish Master_Memo_Dossier_Final.md tracking for SACSCOC CR 6.1"

# 1. Generate the remediated Markdown content
markdown_content = """# Master Memo Dossier: Capital Allocations & Board Compliance
**Document Status:** Public Review Log | Legacy Audit Track
**Classification:** Institutional Governance Framework

## 1. Executive Summary: Hillcrest Asset Evaluation
This dossier outlines historical facility outlays associated with the Hillcrest Advancement Asset. Legacy capital distributions are being transparently logged to ensure absolute alignment with state procurement guidelines and SACSCOC guidelines.

## 2. Remediation of Variance ($850,000.00)
*   **Asset Categorization:** University Advancement Venue and Presidential Residence.
*   **Corrective Action Plan:** Immediate transition of all facility operational logs to the open-access public governance portal.
*   **Fiscal Firewall:** All future structural outlays are subject to a mandatory 60-day public notice period, permanently resolving past administrative transparency gaps.

## 3. Governance Certification
Historical communication delays identified by the audit team have been formally recognized. The institution is establishing an open, bi-weekly reporting cadence with the Faculty Senate to validate compliance parameters.
"""

def deploy_memo():
    # Write the file to the local directory
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(markdown_content.strip())
    print(f"[✓] Local file '{file_name}' successfully created.")

    # Execute git commands sequentially
    try:
        print("[...] Staging file in Git...")
        subprocess.run(["git", "add", file_name], check=True)
        
        print("[...] Committing changes...")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        print("[...] Pushing to main branch...")
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("[★] Deployment complete! The ledger manifest is synchronized.")
        
    except subprocess.CalledProcessError as e:
        print(f"[X] Git Deployment Error: {e}")
    except FileNotFoundError:
        print("[X] Error: Git command line interface not found in your system PATH.")

if __name__ == "__main__":
    deploy_memo()
