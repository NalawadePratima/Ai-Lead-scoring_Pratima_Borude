# api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import redis
from model.predict import predict, rerank

app = FastAPI()
r = redis.Redis(decode_responses=True)

class LeadInput(BaseModel):
    industry: str
    job_title: str
    page_views: int
    time_on_site: float
    emails_opened: int
    past_interactions: int
    notes: str

@app.post("/score")
def score_lead(lead: LeadInput):
    features = lead.dict()
    notes = features.pop("notes")
    cache_key = str(features)

    if r.exists(cache_key):
        return {"cached_score": float(r.get(cache_key))}

    raw_score = predict(features)
    final_score = rerank(raw_score, notes)

    r.set(cache_key, final_score, ex=86400)  # cache for 1 day
    return {"intent_score": final_score}


import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set("test", "hello")
print(r.get("test"))  # Output: hello
