from __future__ import annotations
import numpy as np
import pandas as pd
from config import LEAK_WINDOWS, RANDOM_SEED

def generate_sensor_data(n_samples: int = 1000, seed: int = RANDOM_SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    timestamps = pd.date_range("2026-01-01 09:00:00", periods=n_samples, freq="min")
    t = np.arange(n_samples)
    leak = np.zeros(n_samples, dtype=int)
    for start, end in LEAK_WINDOWS:
        leak[start:end] = 1
    daily = 2.5 * np.sin(2 * np.pi * t / 1440)
    usage = 4.0 * np.sin(2 * np.pi * t / 180)
    flow = 30 + daily + usage + rng.normal(0, 1.3, n_samples)
    pressure = 55 - 0.18 * (flow - 30) + rng.normal(0, 1.0, n_samples)
    level = 72 - 0.015 * np.cumsum(flow - 30) / 10 + rng.normal(0, 0.7, n_samples)
    flow += leak * (12 + rng.normal(0, 1.5, n_samples))
    pressure -= leak * (9 + rng.normal(0, 1.0, n_samples))
    level -= leak * np.linspace(0, 8, n_samples)
    level = np.clip(level, 5, 95)
    return pd.DataFrame({"timestamp": timestamps, "water_flow_lpm": flow, "water_pressure_kpa": pressure, "tank_level_percent": level, "leak": leak})
