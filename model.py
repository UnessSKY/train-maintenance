import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

class PredictiveMaintenanceModel:
    def __init__(self):
        self.failure_model = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", GradientBoostingClassifier(
                n_estimators=400,
                learning_rate=0.03,
                max_depth=4
            ))
        ])
        self.rul_model = RandomForestRegressor(
            n_estimators=300,
            max_depth=10
        )
        self.X = []
        self.y_fail = []
        self.y_rul = []

    def update(self, row):
        features = [
            row["vibration"],
            row["temperature"],
            row["brake_pressure"],
            row["motor_current"],
            row["wheel_rpm"]
        ]
        failure = 1 if row["health"] < 0.3 else 0
        rul = row["health"] * 10000
        self.X.append(features)
        self.y_fail.append(failure)
        self.y_rul.append(rul)

        if len(self.X) > 200:
            self.failure_model.fit(self.X, self.y_fail)
            self.rul_model.fit(self.X, self.y_rul)

    def predict(self, row):
        if len(self.X) < 200:
            return None, None
        features = np.array([[
            row["vibration"],
            row["temperature"],
            row["brake_pressure"],
            row["motor_current"],
            row["wheel_rpm"]
        ]])
        fail_prob = self.failure_model.predict_proba(features)[0][1]
        rul_pred = self.rul_model.predict(features)[0]
        return float(fail_prob), float(rul_pred)
