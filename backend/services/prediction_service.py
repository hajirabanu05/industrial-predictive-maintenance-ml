from backend.ml.predict import predict_failure

from backend.services.severity_service import (
    calculate_severity
)


def predict_machine(sensor):

    result = predict_failure(sensor)

    probability = result["probability"]

    severity_info = calculate_severity(
        probability
    )

    health_status = severity_info[
        "health_status"
    ]

    severity = severity_info[
        "severity"
    ]

    root_causes = []
    recommendations = []

    health_score = max(
        0,
        round(
            (1 - probability) * 100
        )
    )

    if result["prediction"] == "Danger":

        if sensor["Tool wear [min]"] > 200:

            root_causes.append(
                "Excessive tool wear"
            )

            recommendations.append(
                "Replace cutting tool immediately"
            )

        if sensor["Torque [Nm]"] > 60:

            root_causes.append(
                "High torque load"
            )

            recommendations.append(
                "Inspect mechanical load and bearings"
            )

        if (
            sensor["Process temperature [K]"]
            -
            sensor["Air temperature [K]"]
            > 10
        ):

            root_causes.append(
                "High operating temperature"
            )

            recommendations.append(
                "Inspect cooling system"
            )

        if sensor["Rotational speed [rpm]"] > 2500:

            root_causes.append(
                "Excessive rotational speed"
            )

            recommendations.append(
                "Reduce machine speed"
            )

        if not root_causes:

            root_causes.append(
                "Model detected abnormal operating pattern"
            )

            recommendations.append(
                "Schedule maintenance inspection"
            )

    else:

        root_causes.append(
            "Machine operating within normal limits"
        )

        recommendations.append(
            "Continue normal operation"
        )

    return {
        "prediction": result["prediction"],
        "prediction_code": result["prediction_code"],
        "probability": probability,
        "health_status": health_status,
        "severity": severity,
        "health_score": health_score,
        "root_causes": root_causes,
        "recommendations": recommendations
    }