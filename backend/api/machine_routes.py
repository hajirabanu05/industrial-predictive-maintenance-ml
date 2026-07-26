from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.database.crud import save_machine_reading

from backend.services.sensor_service import (
    get_machine_sensor
)

from backend.services.prediction_service import (
    predict_machine
)

router = APIRouter()

MACHINE_COUNT = 3


@router.get("/")
def get_all_machines(
    db: Session = Depends(get_db)
):

    result = []

    for machine_id in range(
        1,
        MACHINE_COUNT + 1
    ):

        sensor = get_machine_sensor(
            machine_id
        )

        prediction = predict_machine(
            sensor
        )

        save_machine_reading(
            db,
            machine_id,
            sensor
        )

        result.append(
            {
                "machine_id": machine_id,
                "sensor": sensor,
                "status": prediction["health_status"],
                "severity": prediction["severity"],
                "health_score": prediction["health_score"],
                "probability": prediction["probability"]
            }
        )

    return result


@router.get("/{machine_id}")
def get_machine(
    machine_id: int,
    db: Session = Depends(get_db)
):

    sensor = get_machine_sensor(
        machine_id
    )

    prediction = predict_machine(
        sensor
    )

    save_machine_reading(
        db,
        machine_id,
        sensor
    )

    return {
        "machine_id": machine_id,
        "sensor": sensor,
        "status": prediction["health_status"],
        "severity": prediction["severity"],
        "health_score": prediction["health_score"],
        "probability": prediction["probability"],
        "root_causes": prediction["root_causes"],
        "recommendations": prediction["recommendations"]
    }