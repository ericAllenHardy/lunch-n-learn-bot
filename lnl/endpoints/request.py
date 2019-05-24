import json
from flask_restplus import Resource, reqparse

from lnl.app_core import api

def json_text(s):
    return json.loads(s)

class RequestHandler(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('payload', type=json_text)

    @api.expect(parser)
    def post(self):
        return 


