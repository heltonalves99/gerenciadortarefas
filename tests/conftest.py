import pytest

from api import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.testing = True

    return app.test_client()