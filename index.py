from flask import \
    Flask
from flask_cors import CORS

from routes.api.v1.dictionary import dictionary_api
from routes.api.v1.sequence import sequence_api

app = Flask(__name__)
CORS(app, resources={r'/*': {"origins": "*"}})

app.register_blueprint(sequence_api)
app.register_blueprint(dictionary_api)


@app.route("/")
def index():
    return "Welcome to the Orb API"
