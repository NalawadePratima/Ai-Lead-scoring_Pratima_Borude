# model/predict.py
import joblib
import pandas as pd

def predict(lead_features):
    model = joblib.load("model/lead_model.pkl")

    columns = joblib.load("model/columns.pkl")  # <- load feature names

    df = pd.DataFrame([lead_features])
    df = pd.get_dummies(df)

    # Add missing columns
    for col in columns:
        if col not in df:
            df[col] = 0
        # Drop extra columns (from unseen categories)
    df = df[columns]
                
    return float(model.predict_proba(df)[0][1])  # intent score

# Reranker placeholder (simulate LLM reranker)
def rerank(score, notes):
    if "urgent" in notes.lower():
        return min(score + 0.1, 1.0)
    return score
