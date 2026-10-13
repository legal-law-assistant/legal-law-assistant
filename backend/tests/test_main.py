
from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_returns_200_and_expected_json():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "legal-assistant-backend",
    }


def test_home_returns_200():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Legal Assistant API is running"
    )


def test_ask_returns_expected_response_structure():
    response = client.post(
        "/api/v1/ask",
        json={
            "question": "Người lao động muốn nghỉ việc thì sao?",
            "conversation_id": None,
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data["answer"], str)
    assert isinstance(data["citations"], list)
    assert data["citation_status"] == "NOT_VALIDATED"
    assert isinstance(data["request_id"], str)
    assert len(data["request_id"]) > 0


def test_ask_rejects_blank_question():
    response = client.post(
        "/api/v1/ask",
        json={
            "question": "     ",
            "conversation_id": None,
        },
    )

    assert response.status_code == 422


def test_ask_rejects_missing_question():
    response = client.post(
        "/api/v1/ask",
        json={"conversation_id": None},
    )

    assert response.status_code == 422


def test_ask_rejects_question_over_2000_characters():
    response = client.post(
        "/api/v1/ask",
        json={
            "question": "a" * 2001,
            "conversation_id": None,
        },
    )
    assert response.status_code == 422


def test_ask_rejects_question_with_only_whitespace():
    response = client.post(
        "/api/v1/ask",
        json={
            "question": "     ",
            "conversation_id": None,
        },
    )
    assert response.status_code == 422
