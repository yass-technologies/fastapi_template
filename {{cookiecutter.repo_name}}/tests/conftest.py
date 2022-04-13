from fastapi.testclient import TestClient
from pytest import fixture

from {{cookiecutter.project_name}}.core.config import API_PREFIX
from {{cookiecutter.project_name}}.main import app


@fixture
def test_client() -> TestClient:
    return TestClient(app)


@fixture
def user_endpoint() -> str:
    return f"{API_PREFIX}/users"
