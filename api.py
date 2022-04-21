from flask import jsonify
from flask import make_response
from flask_restplus import Api
from flask_restplus import Resource

from my_api import api as myApiSpace

myApi = Api(
  version='0.1',
  title='My API',
  description='Testing Flask with API',
  license='MIT',
  contact='Me',
  contact_url='https://github.com/felixdollack',
  doc='/api'
)

myApi.add_namespace(myApiSpace, path='/api')

@myApi.route('/api/ping')
class Ping(Resource):
    def get(self):
        return make_response(jsonify('PONG'), 200)
