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


def test_plugin_manifest():
    r = client.get('/.well-known/ai-plugin.json')
    assert r.status_code == 200


def test_predict():
    r = client.post('/predict', json=[1.0, 1.2, 1.5])
    assert r.status_code == 200
    data = r.json()
    assert 'roi' in data and 'sharpe' in data


def test_risk():
    r = client.get('/risk')
    assert r.status_code == 200


def test_evaluate():
    r = client.get('/evaluate')
    assert r.status_code == 200
