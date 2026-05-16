import os
import tempfile
import pytest
from app import create_app


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'DATABASE': db_path, 'TESTING': True})
    yield app
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_payment_returns_payment(client):
    response = client.get('/payments/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1
    assert data['amount'] == 150.00
    assert data['status'] == 'completed'


def test_get_payment_not_found(client):
    response = client.get('/payments/999')
    assert response.status_code == 404
    assert 'error' in response.get_json()


def test_get_second_payment(client):
    response = client.get('/payments/2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 2
    assert data['status'] == 'pending'
