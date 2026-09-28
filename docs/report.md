# AI-Based IoT Water Leak Detection and Anomaly Monitoring System Using Simulated Sensor Data

## 1. Title Page

Project Title: AI-Based IoT Water Leak Detection and Anomaly Monitoring System Using Simulated Sensor Data  
Domain: Artificial Intelligence for IoT  
Implementation: Python, simulated IoT data, Linear Regression, Isolation Forest, Matplotlib, Streamlit  
Repository: https://github.com/Arbaz-git-hub/ai-iot-water-leak-detection

## 2. Abstract

Water leakage can cause water loss, structural damage, and unnecessary operating costs when abnormal flow remains unnoticed. This project develops a software-only IoT water leak detection system using simulated sensor data and artificial intelligence. Three sensor streams are generated: water-flow rate, water pressure, and tank level. The data is cleaned and transformed into time-series features before being passed through two AI stages. Linear Regression predicts the expected water-flow rate from related sensor measurements and recent observations. Isolation Forest identifies unusual combinations of sensor values without requiring leak labels during anomaly-model training. A multi-signal decision layer combines anomaly status, prediction residual, and pressure deviation to identify probable leaks. The system evaluates both continuous flow prediction and leak classification using MAE, RMSE, R-squared, accuracy, precision, recall, F1-score, and a confusion matrix. A Matplotlib visualization layer and optional Streamlit dashboard provide monitoring outputs. The final implementation is reproducible, hardware-independent, and suitable for demonstrating the complete simulated IoT-to-AI pipeline.

## 3. Introduction

Water systems generate measurable signals such as flow and pressure. A leak can change the normal relationship between these signals. An AI-enabled monitoring system can learn normal behavior and flag observations that differ from expected patterns.

This capstone implements the concept without physical hardware. Synthetic sensor readings reproduce normal operation and predefined leak events. The design therefore focuses on the complete software pipeline: sensor simulation, preprocessing, prediction, anomaly detection, evaluation, and visualization.

## 4. Objectives

1. Generate reproducible simulated readings from at least three water-system sensors.
2. Preprocess the sensor data and create useful time-series features.
3. Predict expected water flow using Linear Regression.
4. Detect abnormal sensor behavior using Isolation Forest and a multi-signal leak decision.
5. Evaluate and visualize the resulting leak-detection performance.

## 5. Related Work / Existing Systems

### Moen Flo Smart Water Monitor and Shutoff

Moen describes FloSense as technology that learns a home's typical water-usage footprint and monitors for irregularities that may indicate a leak. Moen also describes MicroLeak testing and internal water sensing as parts of its smart-water system.

Source: https://shop.moen.com/pages/flo-smart-water-monitor

### Phyn Smart Water Assistant

Phyn describes its Smart Water Assistant as a water monitor that can notify users when a leak is detected. Its Plumbing Check feature analyzes pressure behavior while water use is stopped to identify pressure loss associated with possible leaks.

Sources: https://phyn.com/products/phyn and https://helpcenter.phyn.com/help/what-is-plumbing-check

### Comparison with this project

Commercial systems use physical sensors and product-specific software. This project instead uses simulated flow, pressure, and tank-level data so that the complete AI pipeline can be implemented and evaluated without hardware. The project demonstrates the underlying concepts rather than reproducing a commercial product.

## 6. System Architecture

The system follows:

Sensor Layer -> Connectivity/Data Input -> Processing -> AI Models -> Application Layer

See architecture.svg in the repository.

### Components

- Sensor layer: simulated water flow, pressure, and tank level.
- Connectivity/data input: generated time-series records act as the software representation of sensor transmission.
- Processing layer: sorting, missing-value handling, lag features, rolling statistics, and chronological train/test split.
- Prediction model: Linear Regression.
- Anomaly model: Isolation Forest.
- Decision layer: combines anomaly, flow residual, and pressure deviation.
- Application layer: Matplotlib plots and Streamlit dashboard.

## 7. Dataset / Data Simulation

The dataset contains 1,000 one-minute observations. The simulation is reproducible with random seed 42.

The three sensor variables are:

| Sensor | Unit | Purpose |
|---|---|---|
| Water flow | L/min | Measures water movement |
| Water pressure | kPa | Captures pressure changes associated with abnormal flow |
| Tank level | % | Represents available water level |

Three leak intervals are injected into the simulation. During leak periods, the simulated flow increases while pressure and tank-level behavior change.

The leak field is ground truth for evaluation only and is not supplied to the AI models as a feature.

## 8. Methodology

### Step 1: Simulation
Generate correlated normal readings and controlled leak events.

### Step 2: Preprocessing
Sort timestamps, interpolate missing sensor values, use median fallback where necessary, and create lag/rolling features.

### Step 3: Prediction
Train Linear Regression on the chronological training portion to estimate expected water flow.

### Step 4: Anomaly detection
Train Isolation Forest on sensor-derived features without using the leak label.

### Step 5: Leak decision
Flag a reading when at least one of the following indicates abnormal behavior: Isolation Forest anomaly, prediction residual above 4 L/min, or pressure below 90% of the previous-observation expanding median.

### Step 6: Evaluation
Evaluate flow prediction with MAE, RMSE and R². Evaluate leak classification with accuracy, precision, recall and F1-score.

## 9. Implementation

The main implementation files are:

- src/data_simulation.py
- src/preprocessing.py
- src/models.py
- src/evaluation.py
- src/visualization.py
- src/main.py
- dashboard/app.py

The project can be executed with:

    pip install -r requirements.txt
    python src/main.py

The optional dashboard can be started with:

    python -m streamlit run dashboard/app.py

## 10. Results and Evaluation

For the reproducible seed-42 held-out test segment:

| Metric | Value |
|---|---:|
| Flow MAE | 0.708 L/min |
| Flow RMSE | 0.961 L/min |
| Flow R² | 0.941 |
| Leak accuracy | 97.5% |
| Leak precision | 90.9% |
| Leak recall | 100.0% |
| Leak F1 | 95.2% |

Confusion matrix for seed 42:

    [[145, 5],
     [0, 50]]

The five-seed robustness test on the validated local environment produced RMSE values from 0.928 to 1.013 L/min, R² values from 0.941 to 0.958, precision from 0.847 to 0.909, recall from 0.980 to 1.000, and F1 from 0.917 to 0.952. All five seeds passed the automated robustness guardrails.

## 11. Discussion

The simulation demonstrates that multiple correlated sensor signals can be combined to identify abnormal water-system behavior. Linear Regression provides an interpretable expected-flow baseline, while Isolation Forest supplies an unsupervised anomaly signal. The additional residual and pressure rules help detect sustained leak behavior that may not always be classified as an isolated anomaly.

The main limitation is that the dataset is synthetic. The leak signatures were intentionally designed to be detectable, so the reported metrics cannot be treated as evidence of performance on real plumbing systems. A field deployment would require real sensor calibration, diverse operating conditions, labeled leak events, and validation across different installations.

## 12. Conclusion and Future Scope

The project implements a complete software-only AI-for-IoT water leak detection pipeline. It satisfies the core workflow by simulating sensors, preprocessing the data, using a prediction model, applying an anomaly model, and producing visualization/dashboard outputs.

Future work can include real flow and pressure sensors, MQTT connectivity, edge deployment on a Raspberry Pi or similar device, LSTM-based sequence prediction, adaptive thresholds, alert notifications, and validation on real leak datasets.

## 13. Individual Contribution

The project was developed as a collaborative team effort, with responsibilities distributed across system development, data processing, AI modelling, visualization, testing, documentation, and presentation.

- **Khan Arbaz (251865):** Technical development, system integration, AI modelling, testing, and project coordination.
- **Hawaldar Ziya (251868):** Data and sensor-simulation activities, preprocessing support, and project review.
- **Shaikh Naufil (251869):** Visualization/dashboard review, results organization, and presentation support.
- **Qureshi Fareed (251870):** Documentation, report organization, evaluation review, and presentation support.

All team members should be prepared to explain the complete project pipeline and the methodology during the viva.

## 14. References

1. Moen, Flo Smart Water Monitor and Shut Off. https://shop.moen.com/pages/flo-smart-water-monitor
2. Moen Solutions, FloSense, explained. https://solutions.moen.com/Smart_Water_Security_Products/Help_Center/Flo_by_Moen_app/FloSense%2C_explained
3. Phyn, Smart Water Assistant. https://phyn.com/products/phyn
4. Phyn Help Center, What Is a Plumbing Check? https://helpcenter.phyn.com/help/what-is-a-plumbing-check
5. Scikit-learn documentation for LinearRegression and IsolationForest.
6. Python, NumPy, pandas, Matplotlib and Streamlit documentation.

## 15. Appendix

The complete source code is maintained in the GitHub repository. The tests/test_pipeline.py file contains automated validation cases and docs/TESTING.md records the test results.
