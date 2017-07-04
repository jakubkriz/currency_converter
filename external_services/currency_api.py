# -*- coding: utf-8 -*-

import requests

import strings

class CurrencyApi:
    """
    Represents a service used to get a currency rate between given currencies
    """
    @staticmethod
    def get_rate(currency_input, currency_output):
        url = u"http://api.fixer.io/latest?base={0}&symbols={1}"
        complete_url = url.format(currency_input, currency_output)
        try:
            response = requests.get(complete_url, timeout=3).json()
            if not response.status_code == 200:
                print strings.API_ERROR.format(response.status_code)
                return None
            return response[u'rates'][currency_output]
        except requests.Timeout as exc:
            print strings.API_TIMEOUT
        except KeyError as exc:
            print strings.API_RATE_ERROR
        return None

    @staticmethod
    def get_available_currencies():
        url = u"http://api.fixer.io/latest"
        currencies = []
        try:        
            response = requests.get(url, timeout=3).json()
            if not response.status_code == 200:
                print strings.API_ERROR.format(response.status_code)
                return None
            for currency in response[u'rates'].keys():
                currencies.append(currency) 
            return currencies          
        except requests.Timeout as exc:
            print strings.API_TIMEOUT
        except KeyError as exc:
            print strings.API_CURRENCIES_ERROR
        return None

