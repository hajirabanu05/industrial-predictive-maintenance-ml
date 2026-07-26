import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score
)

from sklearn.model_selection import train_test_split

from backend.config.settings import DATA_PATH


# ------------------------------------
# Load Dataset
# ------------------------------------

df = pd.read_csv(DATA_PATH)

failure_cols = [
    "TWF",
    "HDF",
    "PWF",
    "OSF",
    "RNF"
]

df["failure"] = (
    df[failure_cols]
    .any(axis=1)
    .astype(int)
)

features = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

X = df[features]
y = df["failure"]

# ------------------------------------
# Rename Columns For XGBoost
# ------------------------------------

X.columns = [
    "air_temperature",
    "process_temperature",
    "rotational_speed",
    "torque",
    "tool_wear"
]

# ------------------------------------
# Train Test Split
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# ====================================
# RANDOM FOREST
# ====================================

print("\n========================")
print("Random Forest")
print("========================")

rf = RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42
)

rf.fit(X_train, y_train)

rf_preds = rf.predict(X_test)

print(classification_report(y_test, rf_preds))
print(confusion_matrix(y_test, rf_preds))

rf_f1 = f1_score(y_test, rf_preds)

# ====================================
# XGBOOST
# ====================================

print("\n========================")
print("XGBoost")
print("========================")

xgb = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss"
)

xgb.fit(X_train, y_train)

xgb_preds = xgb.predict(X_test)

print(classification_report(y_test, xgb_preds))
print(confusion_matrix(y_test, xgb_preds))

xgb_f1 = f1_score(y_test, xgb_preds)

# ====================================
# RESULTS
# ====================================

print("\n========================")
print("MODEL COMPARISON")
print("========================")

print(f"Random Forest F1 Score : {rf_f1:.4f}")
print(f"XGBoost F1 Score       : {xgb_f1:.4f}")

if xgb_f1 > rf_f1:
    print("\nWinner: XGBoost")
else:
    print("\nWinner: Random Forest")