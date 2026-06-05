# PRESS BRIEFING: Kentucky State University Forensic Audit

## Executive Summary
This independent forensic audit reveals a pattern of administrative concealment at Kentucky State University (KSU), anchored by a November 2024 Department of Education HCM2 financial lockout and doctored October 2010 board minutes. These findings demonstrate systemic non-compliance concealed from public oversight.

## Core Findings & Evidence Trail
1. **HCM2 Lockout Concealment (November 2024)**  
   * **Finding:** KSU was placed on Heightened Cash Monitoring 2 (HCM2) restrictions by the U.S. Department of Education, completely cutting off automatic federal fund access. This restriction was hidden from the Board of Regents.
   * **Verification:** Run `ksu_fraud_tracker.py` or view static data verification trends in `output/fraud_tracker_results.txt`.

2. **Altered Public Records**  
   * **Finding:** October 2010 board meeting minutes distributed as official PDFs are doctored files returning raw HTML headers rather than authentic document formatting.
   * **Verification:** Run `apa_compliance_check.py` to inspect signature and metadata mutations.

## Technical Methodology
Data verification relies on automated background routines evaluating API payloads, timeline event spacing, and state clawback traces. All tracking algorithms run transparently via GitHub Actions automation to ensure continuous chain-of-custody logging.
