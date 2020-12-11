import requests


def test_hello_world():
    response = requests.get('http://localhost:5000')
    assert response.ok
