ai-lead-scoring-pratima
Trained a GradientBoosting model on leads.csv - Exposed a REST API using FastAPI - Implemented score prediction and business-rule reranking - Cached predictions with Redis
"ai-lead-scoring-pratima" 
"AI Lead Scoring - Pratima Borude"

Overview
A machine learning-based lead scoring system using FastAPI, Gradient Boosting, and Redis caching.

Structure
- `api/main.py`: FastAPI app with `/score` endpoint
- `model/train_model.py`: Trains the model
- `model/predict.py`: Predicts intent score
- `retrain/retrain_model.py`: Retrains the model with new data
- `data/generate_data.py`: Simulates incoming leads
- `utils/monitoring.py`: Tracks retraining/metrics
- `leads.csv`: Main dataset
- `baseline.csv`: Optional baseline for comparisons

Setup Instructions

pip install -r requirements.txt
uvicorn api.main:app --reload
