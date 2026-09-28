# Data

The project generates its own reproducible synthetic IoT dataset because the capstone is software-only.

Run:

```bash
python src/main.py
```

This creates `data/sensor_data.csv` and evaluation outputs.

Sensors:
- water_flow_lpm
- water_pressure_kpa
- tank_level_percent

The simulation also stores a ground-truth `leak` label for evaluation only. The AI models do not receive this label as an input feature.
