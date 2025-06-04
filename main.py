from flask import Flask
from flask_cors import CORS, cross_origin

from api.core.heartbeat import heartbeat_blueprint
from api.notes.notes import notes_blueprint
import db.database as DB

app = Flask(__name__)

#CORS
cors = CORS(app) 
app.config['CORS_HEADERS'] = 'Content-Type'

# DB
DB.init_db()

# Blueprints
app.register_blueprint(heartbeat_blueprint, url_prefix="/heartbeat")
app.register_blueprint(notes_blueprint, url_prefix="/notes")

@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")