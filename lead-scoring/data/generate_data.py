# data/generate_data.py
import pandas as pd
import numpy as np

def generate_lead_data(n=1000):
    np.random.seed(42)
    data = pd.DataFrame({
        'industry': np.random.choice(['tech', 'finance', 'retail'], n),
        'job_title': np.random.choice(['manager', 'director', 'analyst'], n),
        'page_views': np.random.poisson(4, n),
        'time_on_site': np.random.exponential(300, n),
        'emails_opened': np.random.randint(0, 5, n),
        'past_interactions': np.random.randint(0, 10, n),
        'intent': np.random.choice([0, 1], n, p=[0.7, 0.3])  # target
    })
    return data

if __name__ == "__main__":
    df = generate_lead_data()
    df.to_csv("leads.csv", index=False)
