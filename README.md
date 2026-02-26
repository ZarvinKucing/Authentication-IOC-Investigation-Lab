
# Authentication & IOC Investigation Lab

## Overview

This project simulates a structured cybersecurity investigation workflow focused on authentication-related security events and validation of Indicators of Compromise (IOCs).

The lab demonstrates how a security analyst validates suspicious activity by correlating log evidence with external intelligence sources. It is designed to replicate core investigative steps performed during phishing analysis, suspicious login alerts, and malicious indicator validation within a controlled environment.

This project is intended for educational and portfolio purposes.

---

## Project Objectives

* Simulate authentication-related security events
* Validate Indicators of Compromise (IP, Domain, URL, File Hash)
* Perform structured investigation using multiple validation sources
* Classify incidents based on severity level
* Provide remediation recommendations
* Align investigation process with industry security frameworks

---

## Investigation Scope

This lab focuses on the following security scenarios:

### 1️⃣ Suspicious Authentication Activity

* Multiple failed login attempts
* Potential brute-force behavior
* Abnormal login source indicators

### 2️⃣ Indicator of Compromise (IOC) Validation

* IP reputation check
* Domain reputation lookup
* URL analysis and decoding
* File hash verification

### 3️⃣ Phishing & Suspicious Email Analysis

* Email header inspection
* Suspicious URL validation
* Attachment reputation lookup

---

## Investigation Workflow

The structured workflow implemented in this lab:

1. Identify suspicious indicator or authentication anomaly
2. Collect relevant log evidence
3. Perform reputation checks using external intelligence sources
4. Conduct contextual analysis (DNS / WHOIS / decoding)
5. Correlate findings across validation sources
6. Assign severity classification
7. Provide remediation recommendation

This workflow reflects common SOC-level investigation practices.

---

## Severity Classification Model

| Severity | Description                                                   |
| -------- | ------------------------------------------------------------- |
| Critical | Confirmed malicious indicator with high compromise likelihood |
| High     | Strong malicious reputation across multiple sources           |
| Medium   | Suspicious activity requiring monitoring                      |
| Low      | No confirmed malicious evidence                               |

---

## Security Framework Alignment

This project aligns with:

### NIST Cybersecurity Framework

* DE.CM – Security Continuous Monitoring
* RS.AN – Incident Analysis

### ISO 27001

* A.12.4 – Logging and Monitoring
* A.16 – Information Security Incident Management

---

## Core Capabilities

* IOC Reputation Validation (IP, Domain, URL, Hash)
* DNS & WHOIS Lookup
* Email Header Analysis
* URL Decoding (Base64 / UTF-8 / SafeLink normalization)
* Basic sandbox reputation check simulation
* Structured incident severity classification

---

## Technical Requirements

* Python 3.x
* Dependencies listed in `requirements.txt`
* API keys from selected threat intelligence platforms

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Clone the repository:

```bash
git clone <your_repository_url>
```

Navigate to the project directory:

```bash
cd authentication-ioc-investigation-lab
```

Execute the main script:

```bash
python main_file.py
```

During first execution, you will be prompted to configure required API keys.

---

## Security Considerations

* API keys are stored separately and encrypted using symmetric encryption.
* IOC sanitization functionality allows safe sharing of indicators via email.
* This lab is designed for simulated investigation purposes only.

---

## Project Limitations

* This project does not replace a full enterprise SIEM platform.
* Automation scope is intentionally simplified for educational clarity.
* Results depend on external threat intelligence data availability.

---

## Future Enhancements (Optional)

* Bulk IOC validation support
* Basic reporting export (JSON/CSV)
* MITRE ATT&CK technique mapping
* Detection scoring refinement

---

## Conclusion

This lab demonstrates structured authentication event analysis and IOC validation techniques commonly used in security operations.

It highlights investigative reasoning, multi-source validation, severity classification, and remediation planning within a cybersecurity context.

