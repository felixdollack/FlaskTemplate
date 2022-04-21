from flask import jsonify
from flask import make_response
from flask_restplus import Namespace
from flask_restplus import reqparse
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest

api = Namespace('myapi', description='My API endpoints.')

myTestParser = reqparse.RequestParser(bundle_errors=True)
myTestParser.add_argument('message', help='Some message for the server.', location='json')

@api.route('/test')
class Test(Resource):
    @api.doc(parser=myTestParser)
    def post(self):
        args = myTestParser.parse_args()
        msg = args.get('message', '')
        if len(msg) > 0:
            return make_response(jsonify({'message': f'Received: {msg}'}))
        else:
            raise BadRequest()
