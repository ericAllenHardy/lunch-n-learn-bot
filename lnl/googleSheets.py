from typing import Tuple
import os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request

CLIENT_ID = '294186954255-t3odn7trp72235ccah49kb4gkjf77ad1.apps.googleusercontent.com'
CLIENT_SECRET = '5glj-AbiHndNn-j5tawhsWOH'

class SpreadSheet(object):
    def __init__(self, configPath):
        self.sheets = None
        secretsPath = os.path.join(configPath, 'google_client.json')
        self._flow = Flow.from_client_secrets_file(
          secretsPath
        , scopes=['https://www.googleapis.com/auth/drive.file']
        )
        self._flow.redirect_uri = 'https://ericdevfake.localtunnel.me/oauth2/redirect'

    def authorizationUrl(self) -> Tuple[str, str]:
        return self._flow.authorization_url(
          access_type='offline'
        , include_granted_scopes='true'
        )

    def enableSheets(self, code: str):
        self._flow.fetch_token(code=code)
        service = build('sheets', 'v4', credentials=self._flow.credentials)
        self.sheets = service.spreadsheets()

    @property
    def isEnabled(self):
        return self.sheets is not None

