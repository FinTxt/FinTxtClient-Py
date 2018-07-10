# Copyright (c) FinTxt.io. All rights reserved.
#
# This software is confidential and proprietary information.
# You shall use it only in accordance with the terms of the
# license agreement you entered into with FinTxt.io Ltd.

class FinTxtClient(object):

    '''
    Client for accessing the FinTxt API
    '''

    def __init__(self, key = None):

        self._key = key
        self._server = ""

        # Endpoints
        self._languages = ""
        self._live = ""
        self._historic = ""
