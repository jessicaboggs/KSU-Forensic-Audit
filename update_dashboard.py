import json
import os

# Define the absolute file paths based on your desktop repository structure
BASE_DIR = "/Users/jessicaboggs2/Desktop/The Ultimate KSU Forensic Audit"
JSON_PATH = os.path.join(BASE_DIR, "matrix.json")
HTML_PATH = os.path.join(BASE_DIR, "dashboard.html")

def generate_default_json():
    """Generates the comprehensive SACSCOC matrix data dictionary."""
    matrix_data = {
        "university": "Kentucky State University",
        "audit_year": "2026",
        "unrestricted_deficit": "-$59,000,000",
        "operational_runway_days": -280,
        "standards": [
            {
                "code": "KRS 63.080(4)",
                "title": "Statutory Board Removal Trigger",
                "status": "CRITICAL",
                "vulnerability": "Fiduciary Delinquency. Carrying an unmitigated -$59.0M deficit while using closed executive sessions to shield real estate maneuvers (Proposed Farm Purchase) from public tracking.",
                "strategy": "Governor Beshear holds explicit authority to dissolve the non-compliant Board of Regents for gross neglect of duty, subject to full confirmation by a special session of the Kentucky Senate."
            },

            {
                "code": "KRS 63.080(4)",
                "title": "Statutory Board Removal Trigger",
                "status": "CRITICAL",
                "vulnerability": "Fiduciary Delinquency. Carrying an unmitigated -$59.0M deficit while using closed executive sessions to shield real estate maneuvers (Proposed Farm Purchase) from public tracking.",
                "strategy": "Governor Beshear holds explicit authority to dissolve the non-compliant Board of Regents for gross neglect of duty, subject to full confirmation by a special session of the Kentucky Senate."
            },

            {
                "code": "KRS 63.080(4)",
                "title": "Statutory Board Removal Trigger",
                "status": "CRITICAL",
                "vulnerability": "Fiduciary Delinquency. Carrying an unmitigated -$59.0M deficit while using closed executive sessions to shield real estate maneuvers (Proposed Farm Purchase) from public tracking.",
                "strategy": "Governor Beshear holds explicit authority to dissolve the non-compliant Board of Regents for gross neglect of duty, subject to full confirmation by a special session of the Kentucky Senate."
            },

            {
                "code": "Core Requirement 1.1",
                "title": "Institutional Integrity",
                "status": "CRITICAL",
                "vulnerability": "Systemic Candor Breakdown. Omitting mandatory SACSCOC approval contingencies from official press releases; concealing the April 2026 Academic Referral Report.",
                "strategy": "Scrub detailed dockets; run a multi-semester blanket agenda scheme to project an illusion of total control."
            },
            {
                "code": "Core Requirement 2.1",
                "title": "Institutional Mission",
                "status": "CRITICAL",
                "vulnerability": "Mission Subversion. Unilaterally abandoning the traditional liberal arts HBCU mandate to force a compressed polytechnic blueprint without a 5-year cyclical evaluation.",
                "strategy": "Package radical transformations under a generic 'Academic Plan' heading to bypass public mission alteration reviews."
            },
            {
                "code": "Core Requirement 3.1.c",
                "title": "Continuous Operation",
                "status": "CRITICAL",
                "vulnerability": "Operation Interruption. Slashing core degree programs unilaterally under SB 185 before SACSCOC evaluates or authorizes teach-out frameworks.",
                "strategy": "Mask rapid programmatic shutdowns under standard committee headings to dodge immediate teach-out and enrollment scrutiny."
            },
            {
                "code": "Standard 4.1 & 4.2.b",
                "title": "Fiduciary Oversight & Distinction",
                "status": "CRITICAL",
                "vulnerability": "Fiduciary Abandonment. Authorizing a 'Proposed Farm Purchase' despite a -$59M deficit; stuffing adverse compliance failure audits into non-debatable blocks.",
                "strategy": "Bury the devastating CLA Single Audit inside the Consent Agenda; approve macro capital expansions via unitemized blanket votes."
            },
            {
                "code": "Standard 5.2.b",
                "title": "Control of Intercollegiate Athletics",
                "status": "CRITICAL",
                "vulnerability": "Athletic Budget Siphoning. Executing unmonitored internal pool raids ($29.5M) to patch baseline operating payroll; siphoning academic dollars to mask overruns.",
                "strategy": "Omit cost-versus-income athletic ledger comparisons from public files; route asset trace lines behind a closed executive session firewall."
            },
            {
                "code": "Standard 10.3",
                "title": "Archived Information",
                "status": "CRITICAL",
                "vulnerability": "Document Spoliation & Catalog Tampering. Wiping or breaking historical public catalogs and degree tracks to obscure the scale of academic cuts executed under SB 185.",
                "strategy": "Break digital archive links; let network proxies obscure historical degree tracking structures to stop verification of breached contracts."
            },
            {
                "code": "Standard 11.1",
                "title": "Library & Information Resources",
                "status": "CRITICAL",
                "vulnerability": "Starved Learning Infrastructure. Diverting designated student library and technology fees into central treasury cash flows; allowing core database subscriptions to expire.",
                "strategy": "Mask severe library resource depletion and expired database subscriptions under generic 'Faculty Workload' and restructuring headings."
            }
        ]
    }
    return matrix_data

def build_dashboard_html(data):
    """Builds a responsive, visually striking HTML dashboard from the JSON matrix."""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forensic SACSCOC Compliance Matrix</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ background-color: #1e293b; color: #fff; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header h1 {{ margin: 0; font-size: 28px; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 20px; }}
        .stat-card {{ background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); border-left: 5px solid #ef4444; }}
        .stat-card h3 {{ margin: 0 0 10px 0; color: #64748b; font-size: 14px; text-transform: uppercase; }}
        .stat-card p {{ margin: 0; font-size: 24px; font-weight: bold; color: #0f172a; }}
        .matrix-table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
        .matrix-table th {{ background-color: #334155; color: #fff; text-align: left; padding: 12px 15px; font-size: 14px; }}
        .matrix-table td {{ padding: 12px 15px; border-bottom: 1px solid #e2e8f0; font-size: 14px; vertical-align: top; }}
        .matrix-table tr:hover {{ background-color: #f8fafc; }}
        .badge {{ background-color: #fecaca; color: #991b1b; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 11px; }}
        .code {{ font-weight: bold; color: #1e3a8a; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Forensic SACSCOC Compliance Matrix</h1>
            <p>{data['university']} — Timeline Tracking Dashboard ({data['audit_year']})</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Unrestricted Net Deficit</h3>
                <p>{data['unrestricted_deficit']}</p>
            </div>
            <div class="stat-card">
                <h3>Operational Cash Runway</h3>
                <p>{data['operational_runway_days']} Days</p>
            </div>
            <div class="stat-card">
                <h3>Active Violation Tracking</h3>
                <p>{len(data['standards'])} Core Metrics</p>
            </div>
        </div>

        <table class="matrix-table">
            <thead>
                <tr>
                    <th width="20%">SACSCOC Standard</th>
                    <th width="35%">Core Vulnerability & Structural Breakdown</th>
                    <th width="35%">2026 "Shell Game" Firewall Strategy</th>
                    <th width="10%">Status</th>
                </tr>
            </thead>
            <tbody>
"""
    for std in data['standards']:
        html_content += f"""                <tr>
                    <td><span class="code">{std['code']}</span><br><small style="color:#64748b;">{std['title']}</small></td>
                    <td>{std['vulnerability']}</td>
                    <td>{std['strategy']}</td>
                    <td><span class="badge">{std['status']}</span></td>
                </tr>\n"""
                
    html_content += """            </tbody>
        </table>
    </div>
</body>
</html>"""
    return html_content

def main():
    print("🔄 Initializing repository directory scan...")
    
    # 1. Verify or create JSON storage profile
    if not os.path.exists(JSON_PATH):
        print("📁 Base matrix data cache missing. Compiling clear dictionary...")
        data = generate_default_json()
        with open(JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"✅ Created clear raw file path: {JSON_PATH}")
    else:
        print("📖 Reading localized JSON ledger records...")
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

    # 2. Rebuild the interface layout
    print("🔨 Rendering visual dashboard layout components...")
    html_output = build_dashboard_html(data)
    
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html_output)
        
    print(f"🚀 Success. Update pipeline closed. Dashboard ready: {HTML_PATH}")

if __name__ == "__main__":
    main()
