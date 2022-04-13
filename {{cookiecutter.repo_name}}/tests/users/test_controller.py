from fastapi.testclient import TestClient


def test_get_user_list(test_client: TestClient, user_endpoint: str) -> None:
    result = test_client.get(user_endpoint)
    assert isinstance(result.json(), list)
