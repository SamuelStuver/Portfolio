import sys
import pytest
sys.path.append('..')

routes = ["/","/home","/about",]
@pytest.mark.parametrize("route", routes)
def test_routes(client, init_database, route):
    """Start with a blank database."""

    response = client.get(route)

    assert response.status_code == 200
    assert response.data
    assert b'Flask Portfolio' in response.data


if __name__ == "__main__":
    from portfolio import app, db

    app.testing = True
    client = app.test_client()
    response = client.get('/home')
    print(response.__dict__)
    print(response.data)
