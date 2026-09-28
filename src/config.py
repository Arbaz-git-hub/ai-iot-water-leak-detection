from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "outputs"
RANDOM_SEED = 42
N_SAMPLES = 1000
TEST_SIZE = 0.20
LEAK_WINDOWS = [(300, 350), (650, 715), (850, 900)]
