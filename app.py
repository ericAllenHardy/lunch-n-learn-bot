from flask import Flask, jsonify
from flask_restplus import Api, Namespace, Resource, reqparse

from lnl.app_core import app, api
from lnl.endpoints import EventHandler, CommandHandler, RequestHandler

namespace = Namespace('root', path='/')

namespace.add_resource(EventHandler, 'event')
namespace.add_resource(RequestHandler, 'request')
namespace.add_resource(CommandHandler, 'command')

api.add_namespace(namespace, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
