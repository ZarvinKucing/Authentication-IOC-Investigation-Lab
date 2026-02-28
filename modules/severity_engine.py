def calculate_severity(result):
    if result.get("failed_attempts", 0) >= 5:
        return "High"

    if result.get("reputation") == "Malicious":
        return "High"

    if result.get("failed_attempts", 0) > 0:
        return "Medium"

    return "Low"
