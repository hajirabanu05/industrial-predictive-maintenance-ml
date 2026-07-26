from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = BASE_DIR / "data" / "ai4i_clean.csv"

MODEL_PATH = BASE_DIR / "models" / "baseline.joblib"

DATABASE_URL = "sqlite:///maintenance.db"

MACHINE_COUNT = 3