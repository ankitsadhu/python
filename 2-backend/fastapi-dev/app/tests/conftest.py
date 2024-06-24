import pytest
from fastapi.testclient import (
    TestClient,
)  # uses the request lib to maike req against Fastapi app

from app.main import create_application
from app.config import Settings, get_settings


def get_settings_override():
    return Settings(testing=1, environment="dev")


"""
# Scope = "function" | "class" | "module" | "session"
    function - once per test function (default)
    class - once per test class
    module - once per test module
    session - once per test session
"""


@pytest.fixture(scope="module")
def test_app():
    # overrideing dependencies
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        # testing
        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    # configure your db here

    with TestClient(app) as test_client:
        # testing
        yield test_client
