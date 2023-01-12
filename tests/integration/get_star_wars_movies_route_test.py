import json
from app import app

def test_get_movies_route_return_film_title():
    response = app.test_client().get('/character/1/movies')
    data = json.loads(response.data.decode('utf-8'))

    assert data['movies'] == [{"title" :"A New Hope"}, {"title" :"The Empire Strikes Back"}, {"title" :"Return of the Jedi"}, {"title" :"Revenge of the Sith"}, {"title" :"The Force Awakens"}], "Les films retournez ne sont pas bons"
    assert response.status_code == 200
