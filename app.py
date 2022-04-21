from flask import Flask
from my_blueprint import myBlueprint

app = Flask(__name__)
app.register_blueprint(myBlueprint)

@app.route('/hello')
def hello():
    return "<p>Hello, World!</p>"
