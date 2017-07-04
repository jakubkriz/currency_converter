# -*- coding: utf-8 -*-
import json
import requests
from decimal import Decimal

from external_services.currency_api import CurrencyApi
from helpers.parser_helper import ParserHelper
from logger import Logger
import strings

class ConversionManager:
    """
    Represents a main class responsible for currency conversion
    """
    def __init__(self):
        self.logger = Logger()

    def convert_amount(self, amount, input_currency, output_currency=None):
        input_currency = self.__get_input_currency(input_currency)
        output_currencies = self.__get_output_currencies(output_currency)

        input_dict = {
            u'amount': amount, 
            u'currency': input_currency}

        output_dict = {}
        for output_currency in output_currencies:
            try:
                if not input_currency == output_currency:
                    rate = CurrencyApi.get_rate(
                        input_currency, output_currency)
                    if rate:
                        value = Decimal(amount) * Decimal(rate)
                        current_dict = {output_currency: "%0.2f"%value}
                        output_dict.update(current_dict)
                    else:
                        msg = strings.NO_RATE.format(input_currency)
                        output_dict.update({u'error': msg})
            except requests.Timeout as exc:
                self.logger.log_error(strings.API_TIMEOUT)
                return None
            except KeyError as exc:
                msg = strings.API_RATE_ERROR
                msg = msg.format(self.input_currency, output_currency)
                self.logger.log_error(msg)

        return json.dumps({u'input': input_dict, u'output': output_dict})

    def __get_input_currency(self, input_currency):
        # If input currency is a symbol, convert it to currency code
        parser_helper = ParserHelper()
        if parser_helper.is_currency_symbol(input_currency):
            input_currency = \
                parser_helper.get_currency_from_symbol(input_currency)
            if not input_currency:
                msg = strings.SYMBOL_ERROR.format(input_currency)
                self.logger.log_error(msg)
                return None
        return input_currency

    def __get_output_currencies(self, output_currency):
        if not output_currency:
            try:     
                output_currencies = CurrencyApi.get_available_currencies()
                if not output_currencies:
                    output_currencies = self.__get_currencies_from_file()
                else:
                    self.__store_currencies_in_file(output_currencies)
                return output_currencies
            except requests.Timeout as exc:
                self.logger.log_error(strings.API_TIMEOUT)
                return None
            except KeyError as exc:
                self.logger.log_error(strings.API_CURRENCIES_ERROR)
                return None
        else:
            parser_helper = ParserHelper()
            if parser_helper.is_currency_symbol(output_currency):
                output_currency = \
                    parser_helper.get_currency_from_symbol(output_currency)
                if not output_currency:
                    msg = strings.SYMBOL_ERROR.format(input_currency)
                    self.logger.log_error(msg)
                    return None
            return [output_currency]

    def __store_currencies_in_file(self, currencies):
        with open('currencies.txt', 'w') as file:
            for item in currencies:
                file.write("{0}\n".format(item))

    def __get_currencies_from_file(self):
        currencies = []
        with open('currencies.txt') as file:
            currencies = file.readlines()
        # Remove whitespace characters
        currencies = [curr.strip() for curr in currencies] 
        return currencies

