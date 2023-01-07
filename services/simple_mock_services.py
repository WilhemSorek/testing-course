import requests


def get_luke_movies_names() -> list[str]:
    films = requests.get('https://swapi.py4e.com/api/people/1').json()['films']

    array_of_names = []
    for film_url in films:
        r = requests.get(film_url)
        array_of_names.append(r.json()['title'])

    return array_of_names
