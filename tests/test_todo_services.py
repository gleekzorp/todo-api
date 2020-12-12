import pytest
import requests

BASE_URL = 'http://localhost:5000/api/v1'


def test_add_todo():
    payload = {
        "title": "Clean room",
        "done": False
    }
    response = requests.post(f'{BASE_URL}/add-todo', json=payload)
    response_data = response.json()
    assert response.ok
    assert response_data['title'] == 'Clean room'
    assert response_data['done'] is False
    # Not sure if you need to test this
    assert response_data['id']


def test_get_all_todos():
    pytest.xfail()


def test_delete_todo():
    pytest.xfail()


def test_mark_todo_complete():
    pytest.xfail()


def test_delete_all_todos_marked_complete():
    pytest.xfail()