from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from backend.database.connection import Base


class MachineReading(Base):

    __tablename__ = "machine_readings"

    id = Column(
        Integer,
        primary_key=True
    )

    machine_id = Column(
        Integer,
        nullable=False
    )

    air_temperature = Column(Float)

    process_temperature = Column(Float)

    rotational_speed = Column(Float)

    torque = Column(Float)

    tool_wear = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class PredictionRecord(Base):

    __tablename__ = "predictions"

    id = Column(
        Integer,
        primary_key=True
    )

    machine_id = Column(
        Integer,
        nullable=False
    )

    prediction = Column(
        String,
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

    health_score = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )