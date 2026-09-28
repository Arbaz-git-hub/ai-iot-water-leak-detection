# AI-Based IoT Water Leak Detection and Anomaly Monitoring System

Software-only AI for IoT capstone using simulated water-system sensors.

## Pipeline
Simulated Sensors -> Data Preprocessing -> Linear Regression Prediction -> Isolation Forest Anomaly Detection -> Leak Decision -> Visualization / Dashboard

## Sensors
- Water flow rate (L/min)
- Water pressure (kPa)
- Tank level (%)

## Models
- Linear Regression predicts expected water flow and provides MAE, RMSE and R-squared.
- Isolation Forest detects unusual sensor patterns without using the leak label during training.
- A rule combines anomaly status, prediction error and low pressure for the final leak flag.

## Run locally
Python 3.10+ recommended.

pip install -r requirements.txt
python src/main.py

Generated files: data/sensor_data.csv, outputs/test_results.csv, outputs/metrics.json and PNG visualizations.

## Dashboard
streamlit run dashboard/app.py

## Project structure
src/data_simulation.py - reproducible synthetic sensor generation
src/preprocessing.py - cleaning and feature engineering
src/models.py - Linear Regression and Isolation Forest
src/evaluation.py - regression/classification metrics
src/visualization.py - Matplotlib plots
src/main.py - end-to-end pipeline
dashboard/app.py - Streamlit monitoring dashboard
docs/methodology.md - methodology notes

data/README.md - dataset documentation

## Academic note
The system uses simulated data because this capstone is software-only. Ground-truth leak labels are retained for evaluation and are not model input features.
