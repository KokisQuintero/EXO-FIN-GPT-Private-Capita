import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_openapi():
    response = client.get("/openapi.yaml")
    assert response.status_code == 200


def test_explain():
    response = client.get("/explain/ABC")
    assert response.status_code == 200


def test_feedback():
    response = client.post("/feedback", json={"note": "good"})
    assert response.status_code == 200


def test_predict():
    prices = [100, 110, 100]
    response = client.post("/predict", json=prices)
    assert response.status_code == 200
    data = response.json()
    assert "roi" in data and "sharpe" in data


def test_evaluate():
    response = client.get("/evaluate")
    assert response.status_code == 200
