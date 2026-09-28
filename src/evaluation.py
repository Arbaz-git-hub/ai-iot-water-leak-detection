from __future__ import annotations
import json
from pathlib import Path
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,f1_score,mean_absolute_error,mean_squared_error,precision_score,recall_score,r2_score

def evaluate_prediction(y_true,y_pred): return {"MAE":float(mean_absolute_error(y_true,y_pred)),"RMSE":float(mean_squared_error(y_true,y_pred)**0.5),"R2":float(r2_score(y_true,y_pred))}
def evaluate_classification(y_true,y_pred): return {"accuracy":float(accuracy_score(y_true,y_pred)),"precision":float(precision_score(y_true,y_pred,zero_division=0)),"recall":float(recall_score(y_true,y_pred,zero_division=0)),"f1":float(f1_score(y_true,y_pred,zero_division=0)),"confusion_matrix":confusion_matrix(y_true,y_pred).tolist(),"classification_report":classification_report(y_true,y_pred,zero_division=0)}
def save_metrics(metrics:dict,path:Path): path.write_text(json.dumps(metrics,indent=2),encoding="utf-8")
