# --------------------------------
#
# Call the live endpoint
#
# --------------------------------

import requests
import json

from FinTxtClient.exceptions import FinTxtClientException

class live(object):

    '''
    @desc: call the live endpoint
    @params:
        - apiClient: FinTxtAPI object
    @return:
    '''

    def __init__(self, apiClient):

        # Set endpoints
        self._endpoint = "live"
        self._apiClient = apiClient

    def live_one(self, _type, language, q):

        # Checks
        if _type in ['companies', 'commodities']:

            self._type = _type

        else:

            raise FinTxtClientException("type must be one of 'companies' or 'companies'")

        if language in ['total', 'english', 'russian', 'french', 'german', 'arabic']:

            self._language = language

        else:

            raise FinTxtClientException("language {} not supported".format(self._language))

        if type(q) == str:

            self._query = q

        else:

            raise FinTxtClientException("query must be a string")

        # Construct the url
        req = "{}{}/{}/{}?q={}".format(self._apiClient._server, self._endpoint, self._type, self._language, self._query)

        # Call client
        resp = self._apiClient.make_request(req, "GET")

        # return
        return(json.loads(resp.content))
