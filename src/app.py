from flask import Flask
#Import the endpoints
from src.endpoints.hello import hello_endpoint, welcome_endpoint

#Initialize application using flask
app = Flask(__name__)

#register the endpoints
app.register_blueprint(welcome_endpoint, url_prefix="/")
app.register_blueprint(hello_endpoint, url_prefix="/api/v1/hello")

