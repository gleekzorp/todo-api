import os

import pytest


@pytest.fixture
def setup_blank_db_test_file():
    from app import db
    if os.path.exists("../db_test.sqlite"):
        os.remove("../db_test.sqlite")
        db.create_all()
    else:
        db.create_all()
