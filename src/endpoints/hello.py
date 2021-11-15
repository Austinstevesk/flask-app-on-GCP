from flask import Blueprint
from flask.json import jsonify

hello_endpoint = Blueprint(name="endpoint_blueprint", import_name=__name__)
welcome_endpoint = Blueprint(name="welcome_endpoint", import_name=__name__)

@welcome_endpoint.route('/', methods=['GET'])
def welcome():

    return jsonify("Welcome to the application, please navigate to " + 
                    "'api/v1/hello' to see the hello message")

@hello_endpoint.route('/', methods=['GET'])
def hello():

    return jsonify({"Hello Message":"Hello from this endpoint"})

