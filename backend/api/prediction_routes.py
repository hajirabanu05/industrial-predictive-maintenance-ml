from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.connection import get_db

from backend.database.crud import (
    save_prediction,
    save_machine_reading,
    save_alert
)

from backend.services.sensor_service import (
    get_machine_sensor
)

from backend.services.prediction_service import (
    predict_machine
)

from backend.services.alert_service import (
    send_alert
)

router = APIRouter()

MACHINE_COUNT = 3


@router.get("/")
def predict_all(
    db: Session = Depends(get_db)
):

    output = []

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

        print(
            f"[PREDICTION] "
            f"Machine {machine_id} | "
            f"Status={prediction['prediction']} | "
            f"Probability={prediction['probability']}"
        )

        if (
            prediction["prediction"] == "Danger"
            and
            prediction["probability"] >= 0.70
        ):

            print(
                f"[ALERT CHECK] "
                f"Machine {machine_id} qualifies for alert"
            )

            send_alert(
                machine_id,
                prediction["probability"],
                prediction["root_causes"],
                prediction["recommendations"]
            )

            save_alert(
                db,
                machine_id,
                prediction["probability"],
                prediction["severity"],
                prediction["root_causes"][0],
                prediction["recommendations"][0]
            )

        save_machine_reading(
            db,
            machine_id,
            sensor
        )

        save_prediction(
            db,
            machine_id,
            prediction["prediction"],
            prediction["probability"],
            prediction["severity"],
            prediction["health_score"]
        )

        output.append(
            {
                "machine_id": machine_id,
                "sensor": sensor,
                "prediction": prediction
            }
        )

    return output


@router.get("/{machine_id}")
def predict_machine_by_id(
    machine_id: int,
    db: Session = Depends(get_db)
):

    sensor = get_machine_sensor(
        machine_id
    )

    prediction = predict_machine(
        sensor
    )

    print(
        f"[PREDICTION] "
        f"Machine {machine_id} | "
        f"Status={prediction['prediction']} | "
        f"Probability={prediction['probability']}"
    )

    if (
        prediction["prediction"] == "Danger"
        and
        prediction["probability"] >= 0.70
    ):

        print(
            f"[ALERT CHECK] "
            f"Machine {machine_id} qualifies for alert"
        )

        send_alert(
            machine_id,
            prediction["probability"],
            prediction["root_causes"],
            prediction["recommendations"]
        )

        save_alert(
            db,
            machine_id,
            prediction["probability"],
            prediction["severity"],
            prediction["root_causes"][0],
            prediction["recommendations"][0]
        )

    save_machine_reading(
        db,
        machine_id,
        sensor
    )

    save_prediction(
        db,
        machine_id,
        prediction["prediction"],
        prediction["probability"],
        prediction["severity"],
        prediction["health_score"]
    )

    return {
        "machine_id": machine_id,
        "sensor": sensor,
        "prediction": prediction
    }