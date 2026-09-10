from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_health():
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.json() == {"status": "ok"}

def test_analyze():
    reponse = client.post("/analyze", json={"text": "Hello, world!"})
    assert reponse.status_code == 200
    assert reponse.json() == {"character_length": 13, "word_count": 2}