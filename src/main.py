from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(Path(__file__).resolve().parent))
from config import DATA_DIR,OUTPUT_DIR,N_SAMPLES,RANDOM_SEED,TEST_SIZE
from data_simulation import generate_sensor_data
from evaluation import evaluate_classification,evaluate_prediction,save_metrics
from models import predict_and_detect,train_models
from preprocessing import clean_and_engineer,split_features
from visualization import create_plots
def main():
    DATA_DIR.mkdir(exist_ok=True); OUTPUT_DIR.mkdir(exist_ok=True)
    raw=generate_sensor_data(N_SAMPLES,RANDOM_SEED); raw.to_csv(DATA_DIR/"sensor_data.csv",index=False)
    data=clean_and_engineer(raw); train,test,features,target=split_features(data,TEST_SIZE)
    reg,iso=train_models(train,features,target); result=predict_and_detect(reg,iso,test,features)
    pred=evaluate_prediction(result[target],result.predicted_flow_lpm); cls=evaluate_classification(result.leak,result.predicted_leak)
    save_metrics({"prediction":pred,"leak_detection":cls},OUTPUT_DIR/"metrics.json"); result.to_csv(OUTPUT_DIR/"test_results.csv",index=False); create_plots(result,OUTPUT_DIR)
    print("Water Leak Detection pipeline completed."); print("Prediction metrics:",pred); print("Leak detection metrics:",{k:v for k,v in cls.items() if k!="classification_report"})
if __name__=="__main__": main()
