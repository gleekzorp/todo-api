import os

import requests


def test_hello_world():
    response = requests.get('http://localhost:5000')
    assert response.ok


def test_sqlite_file_exists():
    assert os.path.exists('../db.sqlite') is True

