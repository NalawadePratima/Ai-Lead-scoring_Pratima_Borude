# model/train_model.py
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import joblib
from sklearn.model_selection import train_test_split

def train():
    df = pd.read_csv("leads.csv")
    X = df.drop(columns=['intent'])
    X = pd.get_dummies(X)
    y = df['intent']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2)
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, "model/lead_model.pkl")
    joblib.dump(X.columns.tolist(), "model/columns.pkl")  # <- save feature names
    return model

if __name__ == "__main__":
    train()
