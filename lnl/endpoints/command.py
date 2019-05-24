from flask import jsonify
from flask_restplus import Resource, reqparse
from lnl.app_core import api, spreadsheet

class CommandHandler(Resource):
    COMMAND_NAME = '/lunch-n-learn'

    parser = reqparse.RequestParser()
    parser.add_argument('token', type=str)
    parser.add_argument('command', type=str, choices=[COMMAND_NAME])
    parser.add_argument('text', type=str)
    parser.add_argument('response_url', type=str)
    parser.add_argument('trigger_id', type=str)
    parser.add_argument('user_id', type=str)
    parser.add_argument('user_name', type=str)
    parser.add_argument('ssl_check', type=int, required=False)

    @api.expect(parser)
    def post(self):
        args = self.parser.parse_args()
        if args['ssl_check'] == 1:
            return '' 

        subCommand = self._subCommand(args)

        if subCommand == 'authorize':
            if spreadsheet.isEnabled:
                return jsonify({
                  "text": "Already done. Go ahead and plan some lunches!"
                })
            (authUrl, _) = spreadsheet.authorizationUrl()
            connectGoogle = {
              "type": "section"
            , "text": {
                  "type": "mrkdwn"
                , "text": "Click <{}|here> to connect LnL to  Google Sheets".format(authUrl)
                }
            }
            return jsonify({
              'blocks': [connectGoogle]
            })
        elif subCommand == 'hello':
            return jsonify({
              "text": "Hi! Nice to meet you"
            }) 
        elif subCommand == 'help':
            return jsonify({
              "text": "help: TODO" 
            }) 
        elif subCommand == 'request':
            return jsonify({
                
            })
        elif subCommand == 'list':
            return jsonify({
              "text": "There aren't any yet"    
            })

        return jsonify({
          "text": "{} -- Lunch-n-Learn doesn't know how to do that yet".format(subCommand)    
        })

    @staticmethod
    def _subCommand(args):
        text = args['text']
        words = text.strip().split()
        if len(words) > 0:
            return words[0]
        return 'help'


