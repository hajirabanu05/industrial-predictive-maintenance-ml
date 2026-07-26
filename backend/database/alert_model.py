from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from datetime import datetime

from backend.database.connection import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    machine_id = Column(
        Integer,
        nullable=False
    )

    probability = Column(
        Float,
        nullable=False
    )

    severity = Column(
        String,
        nullable=False
    )

    root_cause = Column(
        String
    )

    recommendation = Column(
        String
    )

    acknowledged = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )