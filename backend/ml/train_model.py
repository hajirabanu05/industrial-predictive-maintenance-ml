import pandas as pd

from joblib import dump

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from backend.config.settings import DATA_PATH
from backend.config.settings import MODEL_PATH


def train():

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

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)

    dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train()