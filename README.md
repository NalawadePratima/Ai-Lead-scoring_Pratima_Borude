ai-lead-scoring-pratima_Borude
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


How to Run

1. Install dependencies
   pip install -r requirements.txt
2. Train the model
  python model/train_model.py
3.Run Redis
  redis-server  // Linux
4.Start the API
  uvicorn api.main:app --reload
5.Input example
{
  "industry": "IT",
  "job_title": "Developer",
  "page_views": 10,
  "time_on_site": 5.2,
  "emails_opened": 4,
  "past_interactions": 2,
  "notes": "urgent"
}
6.output example
 {
  "intent_score": 0.78
}
