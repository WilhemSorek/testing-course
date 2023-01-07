import requests


def get_star_war_movies_names(id: str) -> list[str]:
    films = requests.get('https://swapi.py4e.com/api/people/%s' % id).json()['films']

    array_of_names = []
    for film_url in films:
        r = requests.get(film_url)
        array_of_names.append(r.json()['title'])

    return array_of_names
