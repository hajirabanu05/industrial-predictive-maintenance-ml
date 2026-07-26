import pandas as pd

from backend.config.settings import DATA_PATH


class DatasetStreamer:

    def __init__(self):

        self.df = pd.read_csv(DATA_PATH)

        failure_cols = [
            "TWF",
            "HDF",
            "PWF",
            "OSF",
            "RNF"
        ]

        self.df["failure"] = (
            self.df[failure_cols]
            .any(axis=1)
            .astype(int)
        )

        self.failure_rows = (
            self.df[self.df["failure"] == 1]
            .index
            .tolist()
        )

        print(
            f"Dataset loaded successfully. "
            f"Total rows: {len(self.df)} | "
            f"Failure rows: {len(self.failure_rows)}"
        )

        self.machine_indexes = {
            1: 0,
            2: self.failure_rows[50],
            3: self.failure_rows[200]
        }

        print("Machine start positions:")
        print(f"Machine 1 -> Row {self.machine_indexes[1]}")
        print(f"Machine 2 -> Row {self.machine_indexes[2]}")
        print(f"Machine 3 -> Row {self.machine_indexes[3]}")

    def get_machine_row(self, machine_id):

        current_index = self.machine_indexes[machine_id]

        print(
            f"[DATASTREAM] Machine {machine_id} "
            f"using dataset row {current_index}"
        )

        row = self.df.iloc[current_index]

        self.machine_indexes[machine_id] += 1

        if self.machine_indexes[machine_id] >= len(self.df):
            self.machine_indexes[machine_id] = 0

        print(
            f"[DATASTREAM] Machine {machine_id} "
            f"next row will be {self.machine_indexes[machine_id]}"
        )

        return {
            "dataset_row": int(current_index),

            "failure_label": int(row["failure"]),

            "Air temperature [K]":
                float(row["Air temperature [K]"]),

            "Process temperature [K]":
                float(row["Process temperature [K]"]),

            "Rotational speed [rpm]":
                float(row["Rotational speed [rpm]"]),

            "Torque [Nm]":
                float(row["Torque [Nm]"]),

            "Tool wear [min]":
                float(row["Tool wear [min]"])
        }