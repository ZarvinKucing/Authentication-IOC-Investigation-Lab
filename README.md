# Authentication & IOC Investigation Lab

## Overview

This project simulates a structured authentication investigation workflow within a controlled lab environment. It focuses on detecting suspicious login attempts and validating potentially malicious IP/domain indicators.

The objective is to demonstrate log-based analysis, severity classification, and structured security reporting aligned with basic security monitoring practices.

---

## Core Capabilities

* Authentication log analysis (failed login detection)
* Suspicious IP identification
* Simulated IOC reputation validation
* Rule-based severity classification
* Structured investigation report generation

---

## Investigation Workflow

1. Analyze authentication log entries
2. Detect repeated failed login attempts
3. Validate suspicious indicator (IP/domain)
4. Assign severity level
5. Generate investigation summary

---

## Severity Model

| Severity | Criteria                                        |
| -------- | ----------------------------------------------- |
| High     | Multiple failed attempts or malicious indicator |
| Medium   | Suspicious but not confirmed malicious          |
| Low      | No abnormal activity detected                   |

---

## Running the Project

```bash
git clone <your_repository_url>
cd Authentication-IOC-Investigation-Lab
python main.py
```

No external API keys or dependencies required.

---

## Framework Alignment

* NIST CSF – Detect (DE.CM)
* NIST CSF – Respond (RS.AN)

---

## Disclaimer

This project is intended for educational and portfolio purposes only.
