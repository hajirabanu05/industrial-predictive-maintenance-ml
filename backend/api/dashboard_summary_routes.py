from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.database.models import PredictionRecord
from backend.database.alert_model import Alert

router = APIRouter()

MACHINE_COUNT = 3


@router.get("/")
def dashboard_summary(
    db: Session = Depends(get_db)
):

    healthy = 0
    warning = 0
    high_risk = 0
    critical = 0

    for machine_id in range(
        1,
        MACHINE_COUNT + 1
    ):

        latest_prediction = (
            db.query(PredictionRecord)
            .filter(
                PredictionRecord.machine_id == machine_id
            )
            .order_by(
                PredictionRecord.id.desc()
            )
            .first()
        )

        if not latest_prediction:
            continue

        probability = latest_prediction.probability

        if probability >= 0.95:

            critical += 1

        elif probability >= 0.85:

            high_risk += 1

        elif probability >= 0.70:

            warning += 1

        else:

            healthy += 1

    total_alerts = db.query(Alert).count()

    return {
        "machines": MACHINE_COUNT,
        "healthy": healthy,
        "warning": warning,
        "high_risk": high_risk,
        "critical": critical,
        "alerts": total_alerts
    }