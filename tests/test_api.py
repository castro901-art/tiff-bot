"""Contract tests for the FastAPI boundary."""

from fastapi.testclient import TestClient

from tiffbot.api import app


client = TestClient(app)


def test_chat_returns_a_session_and_reply() -> None:
    response = client.post("/chat", json={"message": "Hello"})

    assert response.status_code == 200
    body = response.json()
    assert body["capability"] == "chat"
    assert body["reply"] == "Tiffbot is ready to help."
    assert body["session_id"]


def test_execute_returns_placeholder_acknowledgement() -> None:
    response = client.post(
        "/execute",
        json={"action": "code", "payload": {"language": "python"}},
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "accepted",
        "action": "code",
        "result": "queued:code",
    }
