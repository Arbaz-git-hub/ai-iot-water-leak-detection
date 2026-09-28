from pathlib import Path
import sys
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from config import N_SAMPLES,RANDOM_SEED,TEST_SIZE
from data_simulation import generate_sensor_data
from evaluation import evaluate_classification,evaluate_prediction
from models import predict_and_detect,train_models
from preprocessing import clean_and_engineer,split_features
st.set_page_config(page_title="Water Leak Detection",layout="wide")
st.title("AI-Based IoT Water Leak Detection")
st.caption("Simulated sensors -> preprocessing -> Linear Regression -> Isolation Forest -> leak detection")
@st.cache_data
def run_pipeline():
    raw=generate_sensor_data(N_SAMPLES,RANDOM_SEED); data=clean_and_engineer(raw); train,test,features,target=split_features(data,TEST_SIZE); reg,iso=train_models(train,features,target); return predict_and_detect(reg,iso,test,features)
result=run_pipeline()
a,b,c,d=st.columns(4); a.metric("Readings",len(result)); b.metric("Detected leaks",int(result.predicted_leak.sum())); c.metric("Anomalies",int(result.anomaly.sum())); d.metric("Actual leaks",int(result.leak.sum()))
st.subheader("Sensor readings"); st.line_chart(result.set_index("timestamp")[["water_flow_lpm","water_pressure_kpa","tank_level_percent"]])
st.subheader("Observed vs predicted flow"); st.line_chart(result.set_index("timestamp")[["water_flow_lpm","predicted_flow_lpm"]])
st.subheader("Latest readings"); st.dataframe(result.tail(25),use_container_width=True)
pred=evaluate_prediction(result.water_flow_lpm,result.predicted_flow_lpm); cls=evaluate_classification(result.leak,result.predicted_leak)
a,b,c=st.columns(3); a.metric("Flow RMSE",f"{pred['RMSE']:.2f}"); b.metric("Leak precision",f"{cls['precision']:.2%}"); c.metric("Leak recall",f"{cls['recall']:.2%}")
st.subheader("Evaluation"); st.json({"prediction":pred,"leak_detection":{k:v for k,v in cls.items() if k!="classification_report"}})
