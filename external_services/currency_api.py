# -*- coding: utf-8 -*-

import requests

import strings

class CurrencyAPI:
    """
    Represents a service used to get a currency rate between given currencies
    """
    @staticmethod
    def get_rate(currency_input, currency_output):
        url = u"http://api.fixer.io/latest?base={0}&symbols={1}"
        complete_url = url.format(currency_input, currency_output)
        response = requests.get(complete_url).json()
        try:
            return response[u'rates'][currency_output]
        except KeyError as exc:
            print strings.API_RATE_ERROR
            return None

    @staticmethod
    def get_available_currencies():
        url = u"http://api.fixer.io/latest"
        response = requests.get(url).json()
        currencies = []
        try:        
            for currency in response[u'rates'].keys():
                currencies.append(currency)           
        except KeyError as exc:
            print strings.API_CURRENCIES_ERROR
        return currencies

