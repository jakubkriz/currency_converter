# -*- coding: utf-8 -*-
import json
import requests
from decimal import Decimal

from external_services.currency_api import CurrencyApi
from helpers.parser_helper import ParserHelper
from logger import Logger
from config import TEMP_CURR_FILE
import strings

class ConversionManager(object):
    """
    Represents a main class responsible for currency conversion
    """
    @classmethod
    def convert_amount(self, amount, input_currency, output_currency=None):
        # Obtain a currency code in case a currency symbol was used
        input_currency = self.__get_input_currency(input_currency)
        # Obtain a currency code in case a currency symbol was used
        # If no output currency was defined, get all available currencies
        output_currencies = self.__get_output_currencies(output_currency)

        # Prepare input part of the result JSON
        input_dict = {
            u'amount': amount, 
            u'currency': input_currency}

        # Prepare output part of the result JSON
        output_dict = {}
        # For every output currency, convert the input currency
        for output_currency in output_currencies:
            try:
                # Do not convert between the same currencies
                if not input_currency == output_currency:
                    # Use rate obtained from an external service
                    rate = CurrencyApi.get_rate(
                        input_currency, output_currency)
                    # Success -> update the output part of the result JSON
                    if rate:
                        value = Decimal(amount) * Decimal(rate)
                        current_dict = {output_currency: "%0.2f"%value}
                        output_dict.update(current_dict)
                    # Error occured
                    else:
                        msg = strings.NO_RATE.format(input_currency)
                        output_dict.update({u'error': msg})
            # Request timed out
            except requests.Timeout as exc:
                Logger.log_error(strings.API_TIMEOUT)
                return None
            # The response from the server has an unexpected format 
            except KeyError as exc:
                msg = strings.API_RATE_ERROR
                msg = msg.format(self.input_currency, output_currency)
                Logger.log_error(msg)

        # Output both the input and output part as JSON 
        return json.dumps({u'input': input_dict, u'output': output_dict})

    @classmethod
    def __get_input_currency(self, input_currency):
        # If input currency is a symbol, convert it to currency code
        if ParserHelper.is_currency_symbol(input_currency):
            input_currency = \
                ParserHelper.get_currency_from_symbol(input_currency)
            # Handle errors
            if not input_currency:
                msg = strings.SYMBOL_ERROR.format(input_currency)
                Logger.log_error(msg)
                return None
        return input_currency

    @classmethod
    def __get_output_currencies(self, output_currency):
        # If output currency was not defined, return all available currencies
        if not output_currency:
            try:     
                output_currencies = CurrencyApi.get_available_currencies()
                # If the API returned no data, get them from a file
                # The file contains data from the last API call
                if not output_currencies:
                    output_currencies = self.__get_currencies_from_file()
                # Store the data for the future
                else:
                    self.__store_currencies_in_file(output_currencies)
                return output_currencies
            # Request timed out
            except requests.Timeout as exc:
                Logger.log_error(strings.API_TIMEOUT)
                return None
            # The response from the server has an unexpected format 
            except KeyError as exc:
                Logger.log_error(strings.API_CURRENCIES_ERROR)
                return None
        # Output currency was defined
        else:
            # If output currency is a symbol, convert it to currency code
            if ParserHelper.is_currency_symbol(output_currency):
                output_currency = \
                    ParserHelper.get_currency_from_symbol(output_currency)
                # Handle errors
                if not output_currency:
                    msg = strings.SYMBOL_ERROR.format(input_currency)
                    Logger.log_error(msg)
                    return None
            return [output_currency]

    @classmethod
    def __store_currencies_in_file(self, currencies):
        with open(TEMP_CURR_FILE, 'w') as file:
            for item in currencies:
                file.write("{0}\n".format(item))

    @classmethod
    def __get_currencies_from_file(self):
        currencies = []
        with open(TEMP_CURR_FILE) as file:
            currencies = file.readlines()
        # Remove whitespace characters
        currencies = [curr.strip() for curr in currencies] 
        return currencies

