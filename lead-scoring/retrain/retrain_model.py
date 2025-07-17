# retrain/retrain_model.py
from model.train_model import train
from utils.monitoring import check_drift

def maybe_retrain():
    drift = check_drift()
    if any(score > 0.2 for score in drift.values()):
        print("Significant drift detected. Retraining...")
        train()
    else:
        print("No retraining needed.")

if __name__ == "__main__":
    maybe_retrain()
