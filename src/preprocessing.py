from __future__ import annotations
import pandas as pd

def clean_and_engineer(df: pd.DataFrame) -> pd.DataFrame:
    data=df.copy(); data["timestamp"]=pd.to_datetime(data["timestamp"]); data=data.sort_values("timestamp").reset_index(drop=True)
    numeric=["water_flow_lpm","water_pressure_kpa","tank_level_percent"]
    data[numeric]=data[numeric].interpolate(limit_direction="both").fillna(data[numeric].median())
    data["flow_lag_1"]=data["water_flow_lpm"].shift(1); data["pressure_lag_1"]=data["water_pressure_kpa"].shift(1)
    data["flow_roll_mean_5"]=data["water_flow_lpm"].rolling(5,min_periods=1).mean(); data["flow_roll_std_5"]=data["water_flow_lpm"].rolling(5,min_periods=1).std().fillna(0)
    data["pressure_flow_ratio"]=data["water_pressure_kpa"]/data["water_flow_lpm"].clip(lower=1)
    return data.bfill().ffill()

def split_features(data: pd.DataFrame, test_size: float=0.2):
    features=["water_pressure_kpa","tank_level_percent","flow_lag_1","pressure_lag_1","flow_roll_mean_5","flow_roll_std_5","pressure_flow_ratio"]
    split=int(len(data)*(1-test_size)); return data.iloc[:split].copy(),data.iloc[split:].copy(),features,"water_flow_lpm"
