import pandas as pd

from joblib import load

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import train_test_split

from backend.config.settings import DATA_PATH
from backend.config.settings import MODEL_PATH

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

_, X_test, _, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

model = load(MODEL_PATH)

preds = model.predict(X_test)

print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))