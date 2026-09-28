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
- A multi-signal rule combines anomaly status, prediction residual and pressure deviation for the final leak flag.

## Run locally

Python 3.10+ recommended.

    pip install -r requirements.txt
    python src/main.py

Generated files include sensor_data.csv, test_results.csv, metrics.json and PNG visualizations.

## Dashboard

    python -m streamlit run dashboard/app.py

## Testing

    python -m pytest -q

The automated tests cover reproducibility, leak-event generation, missing-value handling, chronological splitting, model outputs and binary detection labels. See docs/TESTING.md for the recorded robustness results.

## Documentation

- docs/report.md — capstone report draft following the required section structure
- docs/methodology.md — methodology details
- docs/TESTING.md — test cases, bug found, fix and multi-seed validation
- architecture.svg — labeled system architecture diagram
- data/README.md — dataset documentation

## Project structure

- src/data_simulation.py — reproducible synthetic sensor generation
- src/preprocessing.py — cleaning and feature engineering
- src/models.py — Linear Regression and Isolation Forest
- src/evaluation.py — regression/classification metrics
- src/visualization.py — Matplotlib plots
- src/main.py — end-to-end pipeline
- dashboard/app.py — Streamlit monitoring dashboard
- tests/test_pipeline.py — automated tests

## Academic note

The system uses simulated data because this capstone is software-only. Ground-truth leak labels are retained for evaluation and are not model input features.
