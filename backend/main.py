from contextlib import asynccontextmanager
import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database.connection import (
    Base,
    engine
)

from backend.database.models import (
    MachineReading,
    PredictionRecord
)

from backend.database.alert_model import (
    Alert
)

from backend.services.background_prediction_service import (
    prediction_loop
)

from backend.api.machine_routes import (
    router as machine_router
)

from backend.api.prediction_routes import (
    router as prediction_router
)

from backend.api.alert_routes import (
    router as alert_router
)

from backend.api.history_routes import (
    router as history_router
)

from backend.api.dashboard_summary_routes import (
    router as dashboard_summary_router
)

from backend.api.live_status_routes import (
    router as live_status_router
)

from backend.api.machine_status_routes import (
    router as machine_status_router
)

from backend.api.health_routes import (
    router as health_router
)

# ------------------------------------
# Create Database Tables
# ------------------------------------

Base.metadata.create_all(
    bind=engine
)

# ------------------------------------
# Background Prediction Loop
# ------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    asyncio.create_task(
        prediction_loop()
    )

    yield

# ------------------------------------
# FastAPI App
# ------------------------------------

app = FastAPI(
    title="Predictive Maintenance API",
    version="1.0.0",
    lifespan=lifespan
)

# ------------------------------------
# CORS (React Frontend)
# ------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ------------------------------------
# Health
# ------------------------------------

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

# ------------------------------------
# Machines
# ------------------------------------

app.include_router(
    machine_router,
    prefix="/machines",
    tags=["Machines"]
)

# ------------------------------------
# Predictions
# ------------------------------------

app.include_router(
    prediction_router,
    prefix="/predictions",
    tags=["Predictions"]
)

# ------------------------------------
# Alerts
# ------------------------------------

app.include_router(
    alert_router,
    prefix="/alerts",
    tags=["Alerts"]
)

# ------------------------------------
# History
# ------------------------------------

app.include_router(
    history_router,
    prefix="/history",
    tags=["History"]
)

# ------------------------------------
# Dashboard Summary
# ------------------------------------

app.include_router(
    dashboard_summary_router,
    prefix="/dashboard-summary",
    tags=["Dashboard Summary"]
)

# ------------------------------------
# Live Status
# ------------------------------------

app.include_router(
    live_status_router,
    prefix="/live-status",
    tags=["Live Status"]
)

# ------------------------------------
# Machine Status
# ------------------------------------

app.include_router(
    machine_status_router,
    prefix="/machine-status",
    tags=["Machine Status"]
)

# ------------------------------------
# Root Endpoint
# ------------------------------------

@app.get("/")
def root():

    return {
        "status": "running",
        "project": "Predictive Maintenance",
        "version": "1.0.0",
        "machines": 3,
        "docs": "/docs",
        "background_predictions": True,
        "prediction_interval_seconds": 10
    }