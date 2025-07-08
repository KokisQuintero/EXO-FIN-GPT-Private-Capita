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
