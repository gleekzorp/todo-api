import os

import requests

BASE_URL = 'http://localhost:5000/api/v1'


def test_hello_world():
    response = requests.get('http://localhost:5000')
    assert response.ok


def test_setup_blank_db_test_file(setup_blank_db_test_file):
    response = requests.get(f'{BASE_URL}/get-all-todos')
    response_data = response.json()
    assert response.ok
    assert len(response_data) == 0
    assert os.path.exists('../db_test.sqlite') is True
