from __future__ import annotations
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression

def train_models(train,features,target):
    reg=LinearRegression().fit(train[features],train[target])
    iso=IsolationForest(n_estimators=200,contamination=0.06,random_state=42).fit(train[features])
    return reg,iso

def predict_and_detect(model,anomaly_model,data,features):
    result=data.copy()
    result["predicted_flow_lpm"]=model.predict(result[features])
    result["prediction_error"]=result["water_flow_lpm"]-result["predicted_flow_lpm"]
    result["anomaly_score"]=anomaly_model.decision_function(result[features])
    result["anomaly"]=(anomaly_model.predict(result[features])==-1).astype(int)
    baseline=result["water_pressure_kpa"].rolling(30,min_periods=1).median()
    pressure_low=result["water_pressure_kpa"]<baseline*0.88
    excess_flow=result["prediction_error"]>5
    # Isolation Forest remains the primary unsupervised signal; the second branch
    # catches strong simultaneous flow/pressure deviations.
    result["predicted_leak"]=((result["anomaly"]==1)|((excess_flow)&(pressure_low))).astype(int)
    return result
