import os

import pytest
import requests

BASE_URL = 'http://localhost:5000/api/v1'


@pytest.fixture
def setup_blank_db_test_file():
    from app import db
    if os.path.exists("../db_test.sqlite"):
        os.remove("../db_test.sqlite")
        db.create_all()
    else:
        db.create_all()


@pytest.fixture
def setup_test_data(setup_blank_db_test_file):
    mock_data = [
        {
            "title": "Clean room",
            "done": False
        },
        {
            "title": "Wash Car",
            "done": False
        },
        {
            "title": "Cut Hair",
            "done": True
        },
        {
            "title": "Code",
            "done": True
        }
    ]
    for todo in mock_data:
        requests.post(f'{BASE_URL}/add-todo', json=todo)
    response = requests.get(f'{BASE_URL}/get-all-todos')
    return response.json()
