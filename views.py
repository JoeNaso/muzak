import base64
import requests
import os

from flask import app, Flask
app = Flask(__name__)

class SpotifyAuth(object):
    """
        Current auth is for Client Credentials, which prevents indiviudal
        user data access. Will update eventually.
        https://developer.spotify.com/web-api/authorization-guide/#client_credentials_flow

    """
    def __init__(self):
        self.spotify_base = 'https://api.spotify.com/'
        self.auth_base = 'https://accounts.spotify.com/api/token'
        self.client_creds = {
            'client_id': os.environ.get('SPOTIFY_CLIENT'),
            'client_secret': os.environ.get('SPOTIFY_SECRET'),
            'reponse_type': 'code',
            'scopes': None
        }
        self.token = None

    def get_auth_header(self):
        header = self.client_creds
        encoded = base64.b64encode("{}:{}".format(header['client_id'], header['client_secret']))
        headers = {'Authorization': 'Basic {}'.format(encoded)}
        params = {'grant_type': 'client_credentials'}
        res = requests.post(self.auth_base, headers=headers, params=params)
        self.token = res.tojson()['access_token']
        authorized_header = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        return authorized_header

    def get_endpoint_url(self, selection):
        """
        Pass a string to get the desired enrpoint concatenated to the
        spotfy_base

        """
        endpoints = {
            'user': None,
            'user-top': 'v1/me/top/',
            'track': None,
            'artist': None
        }

        if selection not in endpoints or not isinstance(selection, str):
            return None

        endpoint = endpoints.get(selection)
        return self.spotify_base + endpoint

if __name__ == '__main__':
    app.run()