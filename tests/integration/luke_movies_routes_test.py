import json
from app import app


def test_get_luke_movies_route():
    response = app.test_client().get('/')
    data = json.loads(response.data.decode('utf-8'))

    assert len(data['movies']) >= 0, "the list is empty"
    assert response.status_code == 200
