from backend.database.models import (
    MachineReading,
    PredictionRecord
)

from backend.database.alert_model import Alert


def save_machine_reading(
    db,
    machine_id,
    sensor
):

    reading = MachineReading(
        machine_id=machine_id,
        air_temperature=sensor["Air temperature [K]"],
        process_temperature=sensor["Process temperature [K]"],
        rotational_speed=sensor["Rotational speed [rpm]"],
        torque=sensor["Torque [Nm]"],
        tool_wear=sensor["Tool wear [min]"]
    )

    db.add(reading)

    db.commit()

    db.refresh(reading)

    return reading


def save_prediction(
    db,
    machine_id,
    prediction,
    probability,
    severity,
    health_score
):

    record = PredictionRecord(
        machine_id=machine_id,
        prediction=prediction,
        probability=probability,
        severity=severity,
        health_score=health_score
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record


def save_alert(
    db,
    machine_id,
    probability,
    severity,
    root_cause,
    recommendation
):

    alert = Alert(
        machine_id=machine_id,
        probability=probability,
        severity=severity,
        root_cause=root_cause,
        recommendation=recommendation
    )

    db.add(alert)

    db.commit()

    db.refresh(alert)

    return alert