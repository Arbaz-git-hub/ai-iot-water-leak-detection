# Methodology

## 1. Sensor simulation
Three simulated sensors represent water-flow rate, water pressure, and tank level. Normal readings are correlated. During configured leak windows, flow increases, pressure falls, and tank level decreases faster.

## 2. Preprocessing
The pipeline sorts readings chronologically, handles missing numeric values using interpolation with a median fallback, and creates lag/rolling features. A chronological train/test split avoids leaking future observations into training.

## 3. Prediction model
A Linear Regression model predicts observed flow using pressure, tank level, recent flow, and rolling flow behavior. Performance is reported with MAE, RMSE, and R-squared.

## 4. Anomaly model
Isolation Forest is trained on the training data to identify unusual sensor patterns without using the leak label.

## 5. Leak decision
A reading is flagged when the anomaly detector identifies unusual behavior and/or the observed flow differs substantially from the model's expected flow while pressure/flow behavior is abnormal. The ground-truth leak label is used only for evaluation.

## 6. Evaluation
Classification performance uses accuracy, precision, recall, F1-score, and a confusion matrix. Prediction performance uses MAE, RMSE, and R-squared.
