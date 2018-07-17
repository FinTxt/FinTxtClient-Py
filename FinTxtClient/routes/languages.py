# --------------------------------
#
# Call the languages endpoint
#
# --------------------------------

import requests
import json

class languages(object):

    '''
    @desc: call the languages endpoint
    @params:
        - apiClient: FinTxtAPI object
    @return:
    '''

    def __init__(self, apiClient):

        # Set endpoints
        self._endpoint = "languages"
        self._apiClient = apiClient

    def get_languages(self):

        # Construct the url
        req = "{}{}".format(self._apiClient._server, self._endpoint)

        # Call client
        resp = self._apiClient.make_request(req, "GET")

        # return
        return(json.loads(resp.content))
