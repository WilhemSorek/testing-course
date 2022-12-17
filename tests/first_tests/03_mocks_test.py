from unittest import TestCase
from unittest.mock import patch, MagicMock
import requests
from requests.exceptions import Timeout

from services.simple_mock_services import get_luke_movies_names


class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class TestMock(TestCase):
    def test_get_all_luke_movies_names(self):
        expected_names = ['A New Hope', 'The Empire Strikes Back',
                          'Return of the Jedi', 'Revenge of the Sith', 'The Force Awakens']
        responses = {
            'https://swapi.py4e.com/api/people/1': {
                'films': [
                    'https://swapi.py4e.com/api/films/1/',
                    'https://swapi.py4e.com/api/films/2/',
                    'https://swapi.py4e.com/api/films/3/',
                    'https://swapi.py4e.com/api/films/6/',
                    'https://swapi.py4e.com/api/films/7/',
                ]
            },
            'https://swapi.py4e.com/api/films/1/': {'title': 'A New Hope'},
            'https://swapi.py4e.com/api/films/2/': {'title': 'The Empire Strikes Back'},
            'https://swapi.py4e.com/api/films/3/': {'title': 'Return of the Jedi'},
            'https://swapi.py4e.com/api/films/6/': {'title': 'Revenge of the Sith'},
            'https://swapi.py4e.com/api/films/7/': {'title': 'The Force Awakens'},
        }

        with patch.object(requests, 'get', side_effect=lambda url: MockResponse(responses[url])) as request_get_mock:
            result = get_luke_movies_names()

        assert result == expected_names

    def test_get_all_luke_movies_names_when_request_raise_exception(self):
        request_get_mock = patch.object(requests, 'get').start()
        request_get_mock.side_effect = Timeout

        with self.assertRaises(Timeout):
            get_luke_movies_names()

    def test_get_all_luke_movies_names_when_people_request_return_empty_films(self):
        expected_names = []

        with patch.object(requests, 'get', return_value=MockResponse({"films": []})) as request_get_mock:
            result = get_luke_movies_names()

        assert result == expected_names
