from flask import Flask, jsonify
from services.star_wars_movies_service import get_star_war_movies_names

app = Flask(__name__)


@app.route('/hello')
def say_hello_route():
    return jsonify({
        'say': 'hello'
    }), 200


@app.route("/character/<id>/movies")
def get_star_wars_movies_route(id: str):
    movies_names = get_star_war_movies_names(id)

    return jsonify({
        'movies': list([{'title': movie} for movie in movies_names])
    }), 200


if __name__ == '__main__':
    app.debug = True
    app.run()
