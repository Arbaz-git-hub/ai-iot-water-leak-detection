import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from data_simulation import generate_sensor_data
from evaluation import evaluate_classification, evaluate_prediction
from models import predict_and_detect, train_models
from preprocessing import clean_and_engineer, split_features


ROBUSTNESS_SEEDS = [1, 7, 21, 42, 99]


def run_seed(seed: int) -> dict:
    raw = generate_sensor_data(1000, seed)
    data = clean_and_engineer(raw)
    train, test, features, target = split_features(data, 0.2)
    regressor, anomaly_model = train_models(train, features, target)
    result = predict_and_detect(regressor, anomaly_model, test, features)

    prediction = evaluate_prediction(result[target], result["predicted_flow_lpm"])
    classification = evaluate_classification(
        result["leak"], result["predicted_leak"]
    )

    return {
        "seed": seed,
        "RMSE": prediction["RMSE"],
        "R2": prediction["R2"],
        "precision": classification["precision"],
        "recall": classification["recall"],
        "F1": classification["f1"],
    }


def test_five_seed_robustness():
    results = [run_seed(seed) for seed in ROBUSTNESS_SEEDS]

    assert len(results) == 5
    assert all(np.isfinite(row["RMSE"]) for row in results)
    assert all(np.isfinite(row["R2"]) for row in results)
    assert all(0.0 <= row["precision"] <= 1.0 for row in results)
    assert all(0.0 <= row["recall"] <= 1.0 for row in results)
    assert all(0.0 <= row["F1"] <= 1.0 for row in results)

    # Guardrails based on the project's validated synthetic-data behavior.
    assert max(row["RMSE"] for row in results) < 1.10
    assert min(row["F1"] for row in results) > 0.85
    assert min(row["recall"] for row in results) >= 0.95

    print("\nFive-seed robustness results:")
    for row in results:
        print(
            f"seed={row['seed']}: "
            f"RMSE={row['RMSE']:.3f}, "
            f"R2={row['R2']:.3f}, "
            f"precision={row['precision']:.3f}, "
            f"recall={row['recall']:.3f}, "
            f"F1={row['F1']:.3f}"
        )
