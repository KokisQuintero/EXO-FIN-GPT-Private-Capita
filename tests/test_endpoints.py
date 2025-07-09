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
