from flask import Blueprint

heartbeat_blueprint = Blueprint('heartbeat', __name__)

@heartbeat_blueprint.route('/')
def index():
    return {"Value":True}