from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.database.models import PredictionRecord

router = APIRouter()


@router.get("/{machine_id}")
def get_machine_history(
    machine_id: int,
    db: Session = Depends(get_db)
):

    records = (
        db.query(PredictionRecord)
        .filter(
            PredictionRecord.machine_id == machine_id
        )
        .order_by(
            PredictionRecord.created_at.desc()
        )
        .limit(50)
        .all()
    )

    return [
        {
            "probability": r.probability,
            "prediction": r.prediction,
            "timestamp": r.created_at
        }
        for r in reversed(records)
    ]