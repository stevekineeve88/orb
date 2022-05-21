from flask import Flask, render_template
from flask_cors import CORS

from server.modules.orb.managers.orb_manager import OrbManager

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/search/<characters>/<size>", methods=["GET"])
def search(characters: str, size: int):
    orb_manager = OrbManager()
    word_collection = orb_manager.search_words(characters, int(size))
    return {
        "content": word_collection.get_words()
    }, 200


if __name__ == 'main':
    app.run()
