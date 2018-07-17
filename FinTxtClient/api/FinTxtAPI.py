# -----------------------------------------
#
# Basic functionality to call the API
#
# -----------------------------------------

import requests

import FinTxtClient
from FinTxtClient.exceptions import FinTxtClientException

class FinTxtAPI:

    '''
    @desc: Class used to make GET and POST requests to FinTxt API
    @params:
        - key: API key. Defaults to None
        - server: Server that API is hosted on
        - requires_key: does the endpoint require an API key? Defaults to False
    '''

    def __init__(self, server, key = None, requires_key = False):

        # Catch exception
        if key is None and requires_key:

            raise FinTxtClientException("Please supply a valid API key")

        # Set variables
        self._key = key
        if not server.endswith("/"):
            self._server = server + "/"
        else:
            self._server = server
        self._requires_key = requires_key

    def make_request(self, url, method, body = None):

        '''
        @desc: Make a GET/POST request to API
        @params:
            - url: which endpoint to call?
            - method: GET or POST
            - body: request body. Defaults to None
        '''

        # Headers
        headers = {}

        if self._requires_key:

            if not self._key is None:

                headers['API-TOKEN'] = self._key

            else:

                raise FinTxtClientException("Please supply a valid API key")

        resp = None

        if method == 'GET':
            response = requests.get(url, headers=headers)

        elif method == 'POST':
            response = requests.post(url, headers=headers, data=body)
        else:
            raise FinTxtClientException('Method ' + method + ' not supported')

        if response.status_code != 200:
            raise FinTxtClientException("Response: {} - {}".format(response.status_code, response.content))

        ## WARNINGS

        return(response)
