from flask_restplus import Resource, reqparse

from lnl.app_core import api, spreadsheet

class Redirect(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('code', type=str, location='args')

    @api.expect(parser)
    def get(self):
        args = self.parser.parse_args()
        spreadsheet.enableSheets(args['code'])
        print(spreadsheet.sheets)

class Auth(Resource): 
    def get(self):
        pass

class Token(Resource):
    def get(self):
        pass
