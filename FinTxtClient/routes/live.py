# --------------------------------
#
# Call the live endpoint
#
# --------------------------------

import requests

from FinTxtClient.exceptions import FinTxtClientException
from FinTxtClient.checks.checks import checks

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

        '''
        @desc: return the live news intensity for a single commodity or company
        @params:
            - _type: one of 'companies' or 'commodities'
            - language: Filter news intensity values by language. See the '/languages' endpoint for allowed values.
            - q: RIC code for the company for which you want to query news intensity values or name of commodity for which you want to query news intensity values. See documentation for supported commodities.
        @return
        '''

        # Checks
        ch = checks(_type, language)
        ch.check_query(q)

        self._type = _type
        self._language = language
        self._query = q

        # Construct the url
        req = "{}{}/{}/{}?q={}".format(self._apiClient._server, self._endpoint, self._type, self._language, self._query)

        # Call client
        resp = self._apiClient.make_request(req, "GET")

        # return
        return(resp)

    def live_portfolio(self, _type, language, identifiers, weights):

        '''
        @desc: return the live news itensity for a portfolio of commodities or companies
        @params:
            - _type: either one of 'companies' or 'commodities'
            - language: Filter news intensity values by language. See the '/languages' endpoint for allowed values.
            - identifiers: RIC codes for the companies for which you want to query news intensity values or names of commodities for which you want to query news intensity values. See documentation for supported commodities. Note that you cannot mix companies and commodities
            - weights: Weight of each company/commodity in your portfolio in decimal format. Should sum to 1, but the API will still return news intensities if this is not the case. See example section.
        @return:
        '''

        self._endpoint = "portfolio/{}".format(self._endpoint)

        # Checks
        ch = checks(_type, language)
        ch.check_portfolio(identifiers, weights)

        self._request = {
            "identifiers":identifiers,
            "weights":weights,
            "type":_type,
            "language":language
        }

        # Ensure that api token will be passed
        self._apiClient._requires_key = True

        # Make url
        url = "{}{}".format(self._apiClient._server, self._endpoint)

        # Make request
        resp = self._apiClient.make_request(url, "POST", self._request)

        # Return
        return(resp)
