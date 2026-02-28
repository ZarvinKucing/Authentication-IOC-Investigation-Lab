def validate_ioc(ioc):
    simulated_malicious = ["45.23.11.90", "malicious-domain.com"]

    if ioc in simulated_malicious:
        reputation = "Malicious"
        flagged = 2
    else:
        reputation = "Clean"
        flagged = 0

    return {
        "investigation_type": "IOC Validation",
        "ioc_value": ioc,
        "reputation": reputation,
        "flagged_sources": flagged
    }
