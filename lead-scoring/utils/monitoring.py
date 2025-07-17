# utils/monitoring.py
import pandas as pd
from scipy.stats import wasserstein_distance

def check_drift(new_data_path="leads.csv", baseline_path="baseline.csv"):
    new_df = pd.read_csv(new_data_path)
    base_df = pd.read_csv(baseline_path)

    drift_scores = {}
    for col in ['page_views', 'time_on_site', 'emails_opened']:
        drift = wasserstein_distance(base_df[col], new_df[col])
        drift_scores[col] = drift

    return drift_scores
