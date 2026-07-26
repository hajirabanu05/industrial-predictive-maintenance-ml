from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.database.alert_model import Alert

router = APIRouter()


@router.get("/")
def get_alerts(
    db: Session = Depends(get_db)
):

    alerts = (
        db.query(Alert)
        .order_by(
            Alert.created_at.desc()
        )
        .limit(100)
        .all()
    )

    return alerts


@router.put("/{alert_id}/acknowledge")
def acknowledge_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):

    alert = (
        db.query(Alert)
        .filter(
            Alert.id == alert_id
        )
        .first()
    )

    if not alert:

        raise HTTPException(
            status_code=404,
            detail="Alert not found"
        )

    alert.acknowledged = True

    db.commit()

    db.refresh(alert)

    return {
        "message": "Alert acknowledged",
        "alert_id": alert.id
    }


@router.get("/open")
def get_open_alerts(
    db: Session = Depends(get_db)
):

    alerts = (
        db.query(Alert)
        .filter(
            Alert.acknowledged == False
        )
        .order_by(
            Alert.created_at.desc()
        )
        .all()
    )

    return alerts