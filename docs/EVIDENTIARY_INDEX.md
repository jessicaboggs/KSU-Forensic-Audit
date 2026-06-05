# # Master Evidentiary Index & Statutory Alignment


| Exhibit ID | Source Artifact / Log File | Forensic Finding | Statutory / Regulatory Violation | Automated Engine |
| :--- | :--- | :--- | :--- | :--- |
| **EX-001** | `january_2026_financial_core.json` | $-4,534,986 cash position; $2.7M restricted funds swept. | Standard 13.6 (Financial Management) / KRS 164A.560 | `ksu_fraud_tracker.py` |
| **EX-002** | `TAB_E-8_G5_API_Payload_Logs.json` | Missing "payload" and "timestamp" telemetry arrays. | Standard 13.6 (Federal Responsibilities / HCM2) | `apa_compliance_check.py` |
| **EX-003** | `schfile_extract_20260604.txt` | Unencrypted student aid profiles leaked under OPEID 0100196800. | Standard 12.1 (Student Services) / GLBA Mandates | `ksu_opeid_leak_tracer.py` |
| **EX-006** | `ksu_hcm2_validator.py` | Institutional cash runway drops below the mandatory 30-day upfront buffer required for HCM2 manual voucher compliance. | 34 C.F.R. § 668.162(d)(2) Manual Review Standards |
