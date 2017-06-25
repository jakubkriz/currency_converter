# -*- coding: utf-8 -*-

import requests

class XigniteApi:
    """
    Represents a service used to convert a given currency
    """

    @staticmethod
    def convert(currency_input, currency_output, amount):
        url = u"http://globalcurrencies.xignite.com/xGlobalCurrencies.json/ConvertRealTimeValue?From={0}&To={1}&Amount={2}"
        complete_url = url.format(currency_input, currency_output, amount)
        response = requests.get(complete_url).json()
        return response[u'Result']