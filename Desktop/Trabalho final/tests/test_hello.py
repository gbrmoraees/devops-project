import pytest
from flask import Flask
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data.decode() == "Hello, DevOps!"
