# Copyright (c) FinTxt.io. All rights reserved.
#
# This software is confidential and proprietary information.
# You shall use it only in accordance with the terms of the
# license agreement you entered into with FinTxt.io Ltd.

# Logging

class FinTxtClient(object):

    '''
    @desc: Client for accessing the FinTxt API
    @params:
        - key: Key to access premium features of the API. Not needed to access free features
    @return: FinTxtClient object
    '''

    def __init__(self, key = None, server = "127.0.0.1"):

        self._key = key
        self._server = server

    def languages():

        '''
        @desc: call the languages endpoint
        '''

        self._FinTxtAPI = FinTxtAPI(self._key, self.server, requires_key = False)

    def live_one(language, type, q):

        '''
        @desc: call the live endpoint
        '''

        self._FinTxtAPI = FinTxtAPI(self._key, self.server, requires_key = True)

    def historic_one(language, type, date, q):

        '''
        @desc: call the historic endpoint
        '''

        # Check from & to date to see if key is necessary

        self._FinTxtAPI = FinTxtAPI(self._key, self.server, requires_key = False)

    def live_portfolio(language, type, identifiers, weights):

        '''
        @desc: call the live endpoint
        '''

        self._FinTxtAPI = FinTxtAPI(self._key, self.server)

    def historic_portfolio(language, type, date, identifiers, weights):

        '''
        @desc: call the historic endpoint
        '''

        # Check from & to date to see if key is necessary

        self._FinTxtAPI = FinTxtAPI(self._key, self.server)
