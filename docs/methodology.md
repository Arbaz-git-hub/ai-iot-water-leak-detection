# Methodology

## 1. Sensor simulation
Three simulated sensors represent water-flow rate, water pressure, and tank level. Normal readings are correlated. During configured leak windows, flow increases, pressure falls, and tank level decreases faster.

## 2. Preprocessing
The pipeline sorts readings chronologically, handles missing numeric values using interpolation with a median fallback, and creates lag/rolling features. A chronological train/test split avoids using future observations for training.

## 3. Prediction model
A Linear Regression model predicts expected water flow using pressure, tank level, recent flow, and rolling flow behavior. Performance is reported with MAE, RMSE and R-squared.

## 4. Anomaly model
Isolation Forest is trained on the training data to identify unusual sensor patterns without using the leak label.

## 5. Leak decision
The final detector combines three signals: Isolation Forest anomaly status, a positive prediction residual above 4 L/min, and pressure below 90% of the previous-observation expanding median. This keeps the anomaly model in the pipeline while allowing sustained leak behavior to be detected even when one signal alone is weak.

## 6. Evaluation
Classification performance uses accuracy, precision, recall, F1-score and a confusion matrix. Prediction performance uses MAE, RMSE and R-squared. Ground-truth leak labels are used only for evaluation.
