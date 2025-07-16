import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json() == {'status': 'ok'}


def test_openapi():
    r = client.get('/openapi.yaml')
    assert r.status_code == 200


def test_predict():
    r = client.post('/predict', json={'prices': [100, 105, 110]})
    assert r.status_code == 200
    data = r.json()
    assert 'roi' in data
    assert data['roi'] > 0
