# ----------------------------------------------
#
# Basic checks for variables passed by user
#
# ----------------------------------------------

import datetime

from FinTxtClient.exceptions import FinTxtClientException

class checks(object):

    def __init__(self, _type, language):

        '''
        @desc: check basic parameters
        '''

        # Checks
        if _type in ['companies', 'commodities']:

            self._type = _type

        else:

            raise FinTxtClientException("type must be one of 'companies' or 'companies'")

        if language in ['total', 'english', 'russian', 'french', 'german', 'arabic']:

            self._language = language

        else:

            raise FinTxtClientException("language {} not supported".format(self._language))

    def check_query(self, q):

        '''
        @desc: check query
        '''

        if type(q) == str:

            self._query = q

        else:

            raise FinTxtClientException("query must be a string")

    def check_date(self, date):

        '''
        @desc: check if date passed in proper format
        @params:
            - date: date passed by user
        @return:
            - converted date
        '''

        # Format date
        format_str = '%d-%m-%Y'

        # Convert to date
        try:

            date_conv = datetime.datetime.strptime(date, format_str)

        except ValueError:

            raise FinTxtClientException("Date {} not in correct format. Pass the date value as 'DD-MM-YYYY'".format(date))

        return(date_conv)

    def check_portfolio(self, weights, identifiers):

        if not len(weights) == len(identifiers):

            raise FinTxtClientException("Length of identifiers is not equal to length of weights")
