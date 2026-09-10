from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_analyze():
    response = client.post("/analyze", json={"text": "Hello, world!"})
    assert response.status_code == 200
    assert response.json() == {"character_length": 13, "word_count": 2}


def test_analyze_rejects_missing_text():
    response = client.post("/analyze", json={"message": "Hello world"})
    assert response.status_code == 422
