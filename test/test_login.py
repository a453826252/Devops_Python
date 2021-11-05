import pytest
from src.app import app

@pytest.fixture()
def client():
    app.testing = True
    yield app.test_client()

def test_login(client):
    result = client.post('/login',data=dict(username='123456',pwd='123456'),follow_redirects=True)
    assert 200 == result.status_code and b'login success' == result.data
