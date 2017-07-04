# -*- coding: utf-8 -*-
import json
from decimal import Decimal

from external_services.currency_api import CurrencyApi
from helpers.parser_helper import ParserHelper
import strings

class ConversionManager:
    """
    Represents a main class responsible for currency conversion
    """
    def __init__(self, amount, input_currency, output_currency=None):
        self.amount = amount
        self.input_currency = self.__get_input_currency(input_currency)
        self.output_currencies = self.__get_output_currencies(output_currency)

    def convert_amount(self):
        input_dict = {
            u'amount': self.amount, 
            u'currency': self.input_currency}

        output_dict = {}
        for output_currency in self.output_currencies:
            rate = CurrencyApi.get_rate(self.input_currency, output_currency)
            value = Decimal(self.amount) * Decimal(rate)
            current_dict = {output_currency: float(value)}
            output_dict.update(current_dict)

        return json.dumps({u'input': input_dict, u'output': output_dict})

    def __get_input_currency(self, input_currency):
        # If input currency is a symbol, convert it to currency code
        if ParserHelper.is_currency_symbol(input_currency):
            input_currency = self.__get_currency_from_symbol(input_currency)
            if not input_currency:
                print strings.SYMBOL_ERROR.format(input_currency)
                return None
        return input_currency

    def __get_output_currencies(self, output_currency):
        if not output_currency:
            output_currencies = CurrencyApi.get_available_currencies()
            if not output_currencies:
                output_currencies = self.__get_currencies_from_file()
            else:
                self.__store_currencies_in_file(output_currencies)
            return output_currencies
        else:
            if ParserHelper.is_currency_symbol(output_currency):
                output_currency = \
                    self.__get_currency_from_symbol(output_currency)
                if not output_currency:
                    print strings.SYMBOL_ERROR.format(output_currency)
                    return None
            return [output_currency]

    def __get_currency_from_symbol(self, input_currency):
        with open('currency_symbols.json') as file:
            currencies = json.load(file)
            for symbol, codes in currencies.iteritems():
                if input_currency.decode('utf-8') == symbol:
                    # Return the 1st currency code for the given symbol
                    return codes[0]
        return None

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

