from flask_restplus import Resource, reqparse
from lnl.app_core import api

class EventHandler(Resource):
    SUPPORTED_EVENTS = ['url_verification']

    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str, choices=SUPPORTED_EVENTS, required=True)
    parser.add_argument('token', type=str)
    parser.add_argument('challenge', type=str)

    @api.expect(parser)
    def post(self):
        args = self.parser.parse_args()

        if args['type'] == 'url_verification':
            return args['challenge']

        return { 'hello': 'world' }


