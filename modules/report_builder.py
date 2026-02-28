import datetime
import os

def build_report(result, severity):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
====================================
INVESTIGATION SUMMARY
====================================

Timestamp         : {timestamp}
Investigation     : {result.get("investigation_type")}

Details           : {result}
Severity Level    : {severity}

Recommended Actions:
- Review authentication logs
- Monitor suspicious indicators
- Apply access control policies if required
"""

    print(report)

    os.makedirs("reports", exist_ok=True)
    filename = f"reports/report_{timestamp.replace(':', '-')}.txt"

    with open(filename, "w") as f:
        f.write(report)

    print(f"\nReport saved to {filename}")
