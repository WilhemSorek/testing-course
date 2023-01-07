from flask import Flask, jsonify
from services.simple_mock_services import get_luke_movies_names

app = Flask(__name__)


@app.route("/")
def get_luke_movies_route():
    luke_movies_names = get_luke_movies_names()

    return jsonify({
        "movies": list([{"title": movie} for movie in luke_movies_names])
    }), 200


if __name__ == "__main__":
    app.debug = True
    app.run()
