from __future__ import annotations

from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression


def train_models(train, features, target):
    """Train the required prediction and anomaly models."""
    regressor = LinearRegression().fit(train[features], train[target])
    anomaly_model = IsolationForest(
        n_estimators=200,
        contamination=0.06,
        random_state=42,
    ).fit(train[features])
    return regressor, anomaly_model


def predict_and_detect(model, anomaly_model, data, features):
    """Predict normal flow, score anomalies, and combine signals into a leak flag."""
    result = data.copy()
    result["predicted_flow_lpm"] = model.predict(result[features])
    result["prediction_error"] = result["water_flow_lpm"] - result["predicted_flow_lpm"]
    result["anomaly_score"] = anomaly_model.decision_function(result[features])
    result["anomaly"] = (anomaly_model.predict(result[features]) == -1).astype(int)

    # Use only previous pressure observations as the baseline so the current
    # reading cannot make its own leak threshold easier to satisfy.
    pressure_baseline = (
        result["water_pressure_kpa"]
        .expanding()
        .median()
        .shift(1)
        .bfill()
    )
    pressure_drop = result["water_pressure_kpa"] < pressure_baseline * 0.90
    excess_flow = result["prediction_error"] > 4.0

    # The Isolation Forest remains an explicit anomaly model, while the final
    # decision combines three independent leak indicators.
    result["predicted_leak"] = (
        (result["anomaly"] == 1)
        | excess_flow
        | pressure_drop
    ).astype(int)
    return result
