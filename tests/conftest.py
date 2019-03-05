import sys
import pytest

sys.path.append('..')
from portfolio import app, db

@pytest.fixture(scope='module')
def client():
    app.testing = True
    client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    #user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
    #user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    #db.session.add(user1)
    #db.session.add(user2)

    # Commit the changes for the users
    #db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
