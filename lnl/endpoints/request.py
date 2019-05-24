from flask_restplus import Resource

from lnl.app_core import api

class RequestHandler(Resource):
    def post(self):
        return { 'hello': 'world' }


