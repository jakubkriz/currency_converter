# -*- coding: utf-8 -*-

import requests

class CurrencyAPI:
    """
    Represents a service used to get a currency rate between given currencies
    """

    @staticmethod
    def get_rate(currency_input, currency_output):
        url = u"http://api.fixer.io/latest?base={0}&symbols={1}"
        complete_url = url.format(currency_input, currency_output)
        response = requests.get(complete_url).json()
        return response[u'Result']