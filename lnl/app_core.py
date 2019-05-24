from os import path

from flask import Flask
from flask_restplus import Api

from lnl.googleSheets import SpreadSheet

app = Flask(__name__)
api = Api(app)

basePath = path.join(path.dirname(__file__))
spreadsheet = SpreadSheet(path.join(basePath, '../config'))

