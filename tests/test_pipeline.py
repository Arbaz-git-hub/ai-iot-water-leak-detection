import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from data_simulation import generate_sensor_data
from preprocessing import clean_and_engineer, split_features
from models import train_models, predict_and_detect


def test_simulation_reproducibility_and_leak_count():
    a = generate_sensor_data(1000, 42)
    b = generate_sensor_data(1000, 42)
    assert a.equals(b)
    assert a.shape == (1000, 5)
    assert int(a["leak"].sum()) == 165
    assert a["timestamp"].is_monotonic_increasing


def test_preprocessing_handles_missing_and_unsorted_data():
    data = generate_sensor_data(100, 42).sample(frac=1, random_state=7).reset_index(drop=True)
    data.loc[[2, 10], "water_pressure_kpa"] = np.nan
    clean = clean_and_engineer(data)
    assert len(clean) == 100
    assert not clean.isna().any().any()
    assert clean["timestamp"].is_monotonic_increasing


def test_models_return_valid_predictions():
    data = clean_and_engineer(generate_sensor_data(1000, 42))
    train, test, features, target = split_features(data, 0.2)
    reg, iso = train_models(train, features, target)
    result = predict_and_detect(reg, iso, test, features)
    assert len(result) == 200
    assert np.isfinite(result["predicted_flow_lpm"]).all()
    assert set(result["anomaly"].unique()).issubset({0, 1})
    assert set(result["predicted_leak"].unique()).issubset({0, 1})
