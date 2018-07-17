#
#
# Basic functionality to call the API
#
#

import requests

import FinTxtClient
from retinasdk.client.exceptions import FinTxtClientException

class FinTxtAPI:

    def __init__(self, key = None, server, requires_key = False):

        if key is None and requires_key:

            raise FinTxtClientException("Please supply a valid API key")

        self._key = key
        self._server = server
        self._requires_key = requires_key

    def make_request(self, endpoint, method, body, headers={}):

        if not self._server.endswith("/"):
            url = self._server + "/" + endpoint
        else:
            url = self._server + endpoint

        if self._requires_key:
            headers['API-TOKEN'] = self._key

        resp = None

        if method == 'GET':
            response = requests.get(url, headers=headers)

        elif method == 'POST':
            response = requests.post(url, headers=headers, data=body)
        else:
            raise FinTxtClientException('Method ' + method + ' not supported')

        if response.status_code != 200:
            raise FinTxtClientException("Response: {} = {}".format(response.status_code, response.content))

        ## WARNINGS

        return(response)
