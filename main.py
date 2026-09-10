from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AnalysisRequest(BaseModel):
    text: str




@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request: AnalysisRequest):
    # Perform analysis on the text
    return {"character_length" :len(request.text), "word_count": len(request.text.split()),
    }

