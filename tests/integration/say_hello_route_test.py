import json
from app import app


def test_say_hello_route_return_say_property():
    response = app.test_client().get('/hello')
    data = json.loads(response.data.decode('utf-8'))

    assert data['say'] == "hello", "it does not say hello"
    assert response.status_code == 200
