def explain_prediction(sensor):

    causes = []

    recommendations = []

    air_temp = sensor["Air temperature [K]"]

    process_temp = sensor["Process temperature [K]"]

    rpm = sensor["Rotational speed [rpm]"]

    torque = sensor["Torque [Nm]"]

    tool_wear = sensor["Tool wear [min]"]

    # -------------------------
    # Air Temperature
    # -------------------------

    if air_temp > 310:

        causes.append("High Air Temperature")

        recommendations.append(
            "Inspect cooling fans and ventilation system"
        )

    # -------------------------
    # Process Temperature
    # -------------------------

    if process_temp > 320:

        causes.append("High Process Temperature")

        recommendations.append(
            "Check process cooling loop"
        )

    # -------------------------
    # Rotational Speed
    # -------------------------

    if rpm > 1800:

        causes.append("High Rotational Speed")

        recommendations.append(
            "Inspect spindle and motor controller"
        )

    elif rpm < 1200:

        causes.append("Abnormally Low Rotational Speed")

        recommendations.append(
            "Check motor performance and drive system"
        )

    # -------------------------
    # Torque
    # -------------------------

    if torque > 60:

        causes.append("High Torque Load")

        recommendations.append(
            "Inspect bearings and lubrication"
        )

    # -------------------------
    # Tool Wear
    # -------------------------

    if tool_wear > 200:

        causes.append("Excessive Tool Wear")

        recommendations.append(
            "Replace or service tool"
        )

    # -------------------------
    # Safe Machine
    # -------------------------

    if len(causes) == 0:

        causes.append(
            "No abnormal operating conditions detected"
        )

        recommendations.append(
            "Continue normal operation"
        )

    return {
        "root_causes": causes,
        "recommendations": recommendations
    }