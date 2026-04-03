from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_info():
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    assert response.json()["status"] == "running"
