from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.database.models import PredictionRecord

router = APIRouter()

MACHINE_COUNT = 3


@router.get("/")
def machine_status(
    db: Session = Depends(get_db)
):

    result = []

    for machine_id in range(
        1,
        MACHINE_COUNT + 1
    ):

        latest = (
            db.query(PredictionRecord)
            .filter(
                PredictionRecord.machine_id == machine_id
            )
            .order_by(
                PredictionRecord.id.desc()
            )
            .first()
        )

        if not latest:
            continue

        result.append(
            {
                "machine_id": machine_id,
                "prediction": latest.prediction,
                "probability": latest.probability,
                "severity": latest.severity,
                "health_score": latest.health_score
            }
        )

    return result