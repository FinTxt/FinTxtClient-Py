# --------------------------------
#
# Call the historic endpoint
#
# --------------------------------

import requests
import json

from FinTxtClient.exceptions import FinTxtClientException

class historic(object):

    '''
    @desc: call the historic endpoint
    @params:
        - apiClient: FinTxtAPI object
    @return:
    '''

    def __init__(self, apiClient):

        # Set endpoints
        self._endpoint = "historic"
        self._apiClient = apiClient

    def historic_one(self, _type, language, date, q):

        '''
        @desc: return the historic news intensity for a single commodity or company
        @params:
            - _type: one of 'companies' or 'commodities'
            - language: Filter news intensity values by language. See the '/languages' endpoint for allowed values.
            - date: Filter news intensity values by date.
            - q: RIC code for the company for which you want to query news intensity values or name of commodity for which you want to query news intensity values. See documentation for supported commodities.
        @return
        '''





        # Construct the url
        req = "{}{}/{}/{}?q={}".format(self._apiClient._server, self._endpoint, self._type, self._language, self._query)

        # Call client
        resp = self._apiClient.make_request(req, "GET")

        # return
        return(json.loads(resp.content))
