# -*- coding: utf-8 -*-

import requests

import strings
from logger import Logger

class CurrencyApi:
    """
    Represents a service used to get a currency rate between given currencies
    """
    @staticmethod
    def get_rate(currency_input, currency_output):
        url = u"http://api.fixer.io/latest?base={0}&symbols={1}"
        complete_url = url.format(currency_input, currency_output)
        response = requests.get(complete_url, timeout=3)
        if not response.status_code == 200:
            Logger().log_error(strings.API_ERROR.format(response.status_code))
            return None
        return response.json()[u'rates'][currency_output]

    @staticmethod
    def get_available_currencies():
        url = u"http://api.fixer.io/latest"
        currencies = []     
        response = requests.get(url, timeout=3)
        if not response.status_code == 200:
            Logger().log_error(strings.API_ERROR.format(response.status_code))
            return None
        for currency in response.json()[u'rates'].keys():
            currencies.append(currency) 
        # EUR is the base currency, so it is not included in what the API returns
        currencies.append('EUR') 
        return currencies  

