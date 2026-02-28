def analyze_auth_log(file_path):
    failed_attempts = 0
    suspicious_ip = None

    with open(file_path, "r") as file:
        logs = file.readlines()

    for line in logs:
        if "Failed password" in line:
            failed_attempts += 1
            suspicious_ip = line.split("from")[-1].strip()

    return {
        "investigation_type": "Authentication Log",
        "failed_attempts": failed_attempts,
        "suspicious_ip": suspicious_ip
    }
