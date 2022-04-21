from flask import Flask
import werkzeug
# fix import bug
werkzeug.cached_property = werkzeug.utils.cached_property
from api import myApi

app = Flask(__name__)
myApi.init_app(app)

@app.route('/hello')
def hello():
    return "<p>Hello, World!</p>"
