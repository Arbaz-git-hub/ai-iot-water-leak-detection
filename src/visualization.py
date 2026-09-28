from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt

def create_plots(df,output_dir:Path):
    output_dir.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(figsize=(12,5)); ax.plot(df.timestamp,df.water_flow_lpm,label="Observed flow"); ax.plot(df.timestamp,df.predicted_flow_lpm,label="Predicted flow",alpha=.8); leaks=df[df.leak==1]; ax.scatter(leaks.timestamp,leaks.water_flow_lpm,s=12,label="Ground-truth leak"); ax.set_title("Water Flow: Observed vs Predicted"); ax.set_ylabel("Flow (L/min)"); ax.legend(); fig.tight_layout(); fig.savefig(output_dir/"flow_prediction.png",dpi=150); plt.close(fig)
    fig,ax=plt.subplots(figsize=(12,5)); ax.plot(df.timestamp,df.water_pressure_kpa,label="Pressure (kPa)"); ax.plot(df.timestamp,df.tank_level_percent,label="Tank level (%)",alpha=.8); d=df[df.predicted_leak==1]; ax.scatter(d.timestamp,d.water_pressure_kpa,s=10,label="Detected leak"); ax.set_title("Sensor Monitoring and Leak Detection"); ax.legend(); fig.tight_layout(); fig.savefig(output_dir/"sensor_monitoring.png",dpi=150); plt.close(fig)
    fig,ax=plt.subplots(figsize=(6,5)); ax.hist(df.loc[df.anomaly==0,"anomaly_score"],bins=30,alpha=.7,label="Normal"); ax.hist(df.loc[df.anomaly==1,"anomaly_score"],bins=30,alpha=.7,label="Anomaly"); ax.set_title("Isolation Forest Anomaly Scores"); ax.set_xlabel("Decision function score"); ax.legend(); fig.tight_layout(); fig.savefig(output_dir/"anomaly_scores.png",dpi=150); plt.close(fig)
