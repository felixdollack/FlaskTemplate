from flask import Blueprint

myBlueprint = Blueprint('MyBlueprint', __name__)

@myBlueprint.route('/')
def index():
    return "<p>Hello, Blueprint!</p>"
