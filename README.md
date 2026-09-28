# AI-Based IoT Water Leak Detection and Anomaly Monitoring System

Software-only AI for IoT capstone using simulated water-system sensors.

## Project overview

This project demonstrates an end-to-end IoT-to-AI pipeline for detecting probable water leaks from simulated sensor readings. It does **not** require physical IoT hardware.

**Pipeline**

Simulated Sensors -> Data Preprocessing -> Linear Regression Prediction -> Isolation Forest Anomaly Detection -> Leak Decision -> Visualization / Dashboard

## Sensors

- Water flow rate (L/min)
- Water pressure (kPa)
- Tank level (%)

The simulator generates 1,000 one-minute observations with reproducible normal behavior and configured leak events.

## Models

- **Linear Regression** predicts expected water flow and is evaluated with MAE, RMSE and R-squared.
- **Isolation Forest** detects unusual sensor patterns without using the leak label during anomaly-model training.
- A **multi-signal leak rule** combines anomaly status, prediction residual and pressure deviation for the final leak flag.

## Requirements

- Python 3.10 or newer
- pip
- No physical sensors or IoT hardware are required

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/Arbaz-git-hub/ai-iot-water-leak-detection.git
cd ai-iot-water-leak-detection
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the end-to-end pipeline

```bash
python src/main.py
```

This generates the simulated dataset, evaluates the models, saves results, and creates visualizations.

## Dashboard

Start the Streamlit dashboard with:

```bash
python -m streamlit run dashboard/app.py
```

Then open the local address shown by Streamlit, normally `http://localhost:8501`.

**Windows note:** using `python -m streamlit` is recommended instead of the `streamlit` executable because some Windows environments block executable launchers through Application Control policies.

## Testing

Run the complete automated test suite:

```bash
python -m pytest -q
```

Expected result for the validated repository state:

```text
4 passed
```

To display the five-seed robustness metrics:

```bash
python -m pytest tests/test_robustness.py -s
```

The tests cover reproducibility, leak-event generation, missing-value handling, chronological preprocessing, model outputs, binary detection labels, end-to-end evaluation, and five-seed robustness.

See [docs/TESTING.md](docs/TESTING.md) for the detailed test cases and recorded validation results.

## Output files

After running `python src/main.py`:

- `data/sensor_data.csv` — generated simulated sensor dataset
- `outputs/test_results.csv` — held-out test predictions and detection results
- `outputs/metrics.json` — prediction and leak-detection metrics
- `outputs/*.png` — generated Matplotlib visualizations

These generated files are ignored by Git and are not required to run the project.

## Project structure

```text
ai-iot-water-leak-detection/
├── src/
│   ├── config.py
│   ├── data_simulation.py
│   ├── preprocessing.py
│   ├── models.py
│   ├── evaluation.py
│   ├── visualization.py
│   └── main.py
├── dashboard/
│   └── app.py
├── tests/
│   ├── test_pipeline.py
│   └── test_robustness.py
├── docs/
│   ├── methodology.md
│   ├── TESTING.md
│   └── report.md
├── data/
│   └── README.md
├── architecture.svg
├── requirements.txt
└── README.md
```

## Documentation

- [docs/report.md](docs/report.md) — capstone report draft following the required section structure
- [docs/methodology.md](docs/methodology.md) — methodology and model logic
- [docs/TESTING.md](docs/TESTING.md) — test cases, issue/fix history and robustness validation
- [architecture.svg](architecture.svg) — system architecture diagram
- [data/README.md](data/README.md) — dataset documentation

## Academic note

The system uses simulated data because the capstone is software-only. Ground-truth leak labels are retained for evaluation and are **not** supplied to the AI models as input features. The reported metrics describe this synthetic simulation and should not be interpreted as real-world field accuracy.

## Reproducibility

The default simulation uses random seed 42. The robustness test additionally validates seeds 1, 7, 21, 42 and 99.
