import asyncio

from backend.database.connection import SessionLocal

from backend.database.crud import (
    save_machine_reading,
    save_prediction,
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


async def prediction_loop():

    while True:

        db = SessionLocal()

        try:

            for machine_id in [1, 2, 3]:

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

                save_prediction(
                    db,
                    machine_id,
                    prediction["prediction"],
                    prediction["probability"],
                    prediction["severity"],
                    prediction["health_score"]
                )

                if (
                    prediction["prediction"] == "Danger"
                    and prediction["probability"] >= 0.70
                ):

                    alert_sent = send_alert(
                        machine_id,
                        prediction["probability"],
                        prediction["root_causes"],
                        prediction["recommendations"]
                    )

                    if alert_sent:

                        save_alert(
                            db,
                            machine_id,
                            prediction["probability"],
                            prediction["severity"],
                            prediction["root_causes"][0],
                            prediction["recommendations"][0]
                        )

        finally:

            db.close()

        await asyncio.sleep(10)