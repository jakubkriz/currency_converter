# -*- coding: utf-8 -*-

import requests

import strings
from logger import Logger

class CurrencyApi(object):
    """
    Represents a service used to get a currency rate between given currencies
    """
    @staticmethod
    def get_rate(currency_input, currency_output):
        url = u"http://api.fixer.io/latest?base={0}&symbols={1}"
        complete_url = url.format(currency_input, currency_output)
        # Get rate from the API
        response = requests.get(complete_url, timeout=3)
        # Error in processing the request occured
        if not response.status_code == 200:
            Logger().log_error(strings.API_ERROR.format(response.status_code))
            return None
        # Success -> return the rate
        return response.json()[u'rates'][currency_output]

    @staticmethod
    def get_available_currencies():
        url = u"http://api.fixer.io/latest"
        currencies = []     
        # Get all available currencies except the base currency - EUR
        response = requests.get(url, timeout=3)
        # Error in processing the request occured
        if not response.status_code == 200:
            Logger().log_error(strings.API_ERROR.format(response.status_code))
            return None
        # Create list of currency codes from the data obtained from the API
        for currency in response.json()[u'rates'].keys():
            currencies.append(currency) 
        # EUR is the base currency and it is not included in what the API returns
        currencies.append('EUR') 
        
        return currencies  

