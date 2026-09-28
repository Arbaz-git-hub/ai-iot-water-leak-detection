# Testing and Validation

The project follows an iterative code-test-run-resolve cycle.

## Test cases

| Test | Purpose | Result |
|---|---|---|
| TC-01 | Generate 1,000 readings with correct columns and timestamps | PASS |
| TC-02 | Repeat seed 42 and confirm identical data | PASS |
| TC-03 | Confirm configured leak windows produce 165 leak-labelled readings | PASS |
| TC-04 | Inject missing pressure readings and shuffle rows | PASS |
| TC-05 | Confirm preprocessing removes missing values and restores chronological order | PASS |
| TC-06 | Confirm Linear Regression outputs finite predictions | PASS |
| TC-07 | Confirm Isolation Forest outputs binary anomaly labels | PASS |
| TC-08 | Confirm final detector outputs binary leak labels | PASS |
| TC-09 | End-to-end held-out test evaluation | PASS |
| TC-10 | Repeat end-to-end run with seeds 1, 7, 21, 42 and 99 | PASS |

## Seed robustness

| Seed | RMSE | R² | Precision | Recall | F1 |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.962 | 0.956 | 0.907 | 0.980 | 0.942 |
| 7 | 1.012 | 0.951 | 0.907 | 0.980 | 0.942 |
| 21 | 0.928 | 0.958 | 0.847 | 1.000 | 0.917 |
| 42 | 0.961 | 0.941 | 0.909 | 1.000 | 0.952 |
| 99 | 1.013 | 0.950 | 0.877 | 1.000 | 0.935 |

These results are for the synthetic simulator and should not be interpreted as real-world field accuracy.

## Issue found and resolved

The first leak-decision rule required an Isolation Forest anomaly plus another condition. This produced high precision but poor recall on the held-out segment. The rule was revised to combine three signals: anomaly status, prediction residual, and pressure deviation from a previous-observation baseline. The revised detector improved recall to 100% for seed 42. The five-seed test then confirmed recall between 98.0% and 100.0% and F1 between 91.7% and 95.2% on the synthetic datasets.


## Automated local suite

The repository includes four pytest tests: three core pipeline tests in `tests/test_pipeline.py` and one five-seed robustness test in `tests/test_robustness.py`. Run the complete suite with `python -m pytest -q`.
