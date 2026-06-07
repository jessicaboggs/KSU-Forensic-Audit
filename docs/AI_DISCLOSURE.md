FORMAL TECHNOLOGICAL & AI DISCLOSURE STATEMENT
## AUTHORITY: KENTUCKY BAR ASSOCIATION (KBA) LEGAL TECHNOLOGY ETHICS FRAMEWORK

This project utilizes advanced artificial intelligence systems for data synthesis, document organization, and cross-referencing. In strict compliance with the ethical parameters established by the Kentucky Bar Association's technology resource guidelines, the investigator certifies the following boundaries of operation:

1. **Independent Data Custody:** Every underlying document, spreadsheet, and legislative index housed across TABS B and C was sourced independently from public repositories, including the Kentucky Legislative Research Commission, the Council on Postsecondary Education, and the Internet Archive's Wayback Machine. No data was fabricated or retroactively generated.
2. **Analytical Integrity & Algorithmic Parsing:** Artificial intelligence and automated local Python execution scripts (specifically 'parse_ppa.py') were deployed strictly as tools for computational logic. This includes isolating specific fixed-width byte bounds (e.g., indices 0:7, 23:31, 39:45) from raw 45-character server strings to accurately decode institutional timelines. AI was utilized to filter, catalog, and structure these public, unscrubbed records into a cohesive chronological timeline. No code was executed externally on proprietary server data, and all outputs have been manually cross-referenced and verified against the official Kentucky Council on Postsecondary Education financial update disclosures to ensure 100% computational accuracy.


### 💻 Implementation Reference: `parse_ppa.py`
The computational logic utilized to enforce this fixed-width isolation layer is structured as follows:

```python
def decode_server_string(raw_string: str) -> dict:
    """
    Decodes specific fixed-width byte bounds from raw 45-character server strings
    to verify unscrubbed timelines against CPE disclosures.
    """
    if len(raw_string) != 45:
        raise ValueError("Server string must be exactly 45 characters.")
        
    return {
        "institution_id":  raw_string[0:7].strip(),    # Indices 0:7
        "timeline_status": raw_string[23:31].strip(),  # Indices 23:31
        "compliance_code": raw_string[39:45].strip()   # Indices 39:45
    }
```

3. **The Principle of Candor:** Unlike the subject administration, which utilized automated scripts to program HTTP 302 redirect loops to hide compliance data, this investigation operates under a policy of total transparency. This disclosure is appended proactively to satisfy the highest expectations of honesty under SACSCOC Core Requirement 1.1.