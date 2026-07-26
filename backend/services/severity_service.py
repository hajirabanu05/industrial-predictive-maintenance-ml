def calculate_severity(probability):

    if probability >= 0.95:

        return {
            "health_status": "Critical",
            "severity": "CRITICAL"
        }

    elif probability >= 0.85:

        return {
            "health_status": "High Risk",
            "severity": "HIGH"
        }

    elif probability >= 0.70:

        return {
            "health_status": "Warning",
            "severity": "MEDIUM"
        }

    return {
        "health_status": "Healthy",
        "severity": "LOW"
    }