# Copyright (c) FinTxt.io. All rights reserved.
#
# This software is confidential and proprietary information.
# You shall use it only in accordance with the terms of the
# license agreement you entered into with FinTxt.io Ltd.

from FinTxtClient.api.FinTxtAPI import FinTxtAPI
from FinTxtClient.routes.languages import languages
from FinTxtClient.routes.live import live
from FinTxtClient.routes.historic import historic

class FinTxtClient(object):

    '''
    @desc: Client for accessing the FinTxt API
    @params:
        - key: Key to access premium features of the API. Not needed to access free features
    @return: FinTxtClient object
    '''

    def __init__(self, key = None, server = "http://127.0.0.1:8000"):

        self._key = key
        self._server = server

    def languages(self):

        '''
        @desc: call the languages endpoint
        '''

        self._FinTxtAPI = FinTxtAPI(self._server, self._key, requires_key = False)

        # Call languages endpoint
        return(languages(self._FinTxtAPI).get_languages())

    def live_one(self, _type, language, q):

        '''
        @desc: call the live endpoint for a single commodity or company
        '''

        self._FinTxtAPI = FinTxtAPI(self._server, self._key, requires_key = True)

        # Call live endpoint
        return(live(self._FinTxtAPI).live_one(_type, language, q))

    def historic_one(self, _type, language, date, q):

        '''
        @desc: call the historic endpoint
        '''

        self._FinTxtAPI = FinTxtAPI(self._server, self._key, requires_key = False)

        # Call historic endpoint
        return(historic(self._FinTxtAPI).historic_one(_type, language, date, q))

    def live_portfolio(self, _type, language, identifiers, weights):

        '''
        @desc: call the live portfolio endpoint
        '''

        self._FinTxtAPI = FinTxtAPI(self._server, self._key, requires_key = True)

        # Call live portfolio endpoint
        return(live(self._FinTxtAPI).live_portfolio(_type, language, identifiers, weights))

    def historic_portfolio(self, _type, language, date, identifiers, weights):

        '''
        @desc: call the historic endpoint
        '''

        self._FinTxtAPI = FinTxtAPI(self._server, self._key, requires_key = False)

        # Call historic portfolio endpoint
        return(historic(self._FinTxtAPI).historic_portfolio(_type, language, date, identifiers, weights))
