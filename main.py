from modules.auth_analyzer import analyze_auth_log
from modules.ioc_validator import validate_ioc
from modules.severity_engine import calculate_severity
from modules.report_builder import build_report

def main():
    print("=== Authentication & IOC Investigation Lab ===")
    print("1. Analyze Authentication Log")
    print("2. Validate IOC")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        result = analyze_auth_log("sample_logs/auth.log")
        severity = calculate_severity(result)
        build_report(result, severity)

    elif choice == "2":
        ioc = input("Enter IP or Domain: ")
        result = validate_ioc(ioc)
        severity = calculate_severity(result)
        build_report(result, severity)

    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
