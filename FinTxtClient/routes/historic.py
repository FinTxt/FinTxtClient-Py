# --------------------------------
#
# Call the historic endpoint
#
# --------------------------------

import requests
import datetime

from FinTxtClient.exceptions import FinTxtClientException
from FinTxtClient.checks.checks import checks

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

        # Checks
        ch = checks(_type, language)

        # Check query
        ch.check_query(q)

        # Check date
        date_conv = ch.check_date(date)

        ## Filter dates
        current = datetime.date.today()
        free = current - datetime.timedelta(30)

        # Needs key if want this endpoint
        if date_conv >= free:

            self._apiClient._requires_key = True

        self._type = _type
        self._language = language
        self._query = q
        self._date = date

        # Construct the url
        req = "{}{}/{}/{}/{}?q={}".format(self._apiClient._server, self._endpoint, self._type, self._language, self._date, self._query)

        # Call client
        resp = self._apiClient.make_request(req, "GET")

        # return
        return(resp)

    def historic_portfolio(self, _type, language, date, identifiers, weights):

        '''
        @desc: return the historic news itensity for a portfolio of commodities or companies
        @params:
            - _type: either one of 'companies' or 'commodities'
            - language: Filter news intensity values by language. See the '/languages' endpoint for allowed values.
            - date: Filter news intensity values by date.
            - identifiers: RIC codes for the companies for which you want to query news intensity values or names of commodities for which you want to query news intensity values. See documentation for supported commodities. Note that you cannot mix companies and commodities
            - weights: Weight of each company/commodity in your portfolio in decimal format. Should sum to 1, but the API will still return news intensities if this is not the case. See example section.
        @return:
        '''

        self._endpoint = "portfolio/{}".format(self._endpoint)

        # Checks
        ch = checks(_type, language)
        # Check date
        date_conv = ch.check_date(date)
        ch.check_portfolio(identifiers, weights)

        ## Filter dates
        current = datetime.date.today()
        free = current - datetime.timedelta(30)

        # Needs key if want this endpoint
        if current >= free:

            self._apiClient._requires_key = True

        self._request = {
            "identifiers":identifiers,
            "weights":weights,
            "type":_type,
            "date":date,
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
