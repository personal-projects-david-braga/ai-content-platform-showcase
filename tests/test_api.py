from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_rejects_invalid_deck() -> None:
    response = client.post("/v1/decks/validate", json={"title": "Demo", "slides": []})
    assert response.status_code == 422
