from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.incidents import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_create_and_list():
    r = client.post("/incidents", params={"title": "test"})
    assert r.status_code == 200

    r = client.get("/incidents")
    assert r.status_code == 200
    assert len(r.json()) >= 1
