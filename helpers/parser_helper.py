# -*- coding: utf-8 -*-

import argparse
import re
import json

from logger import Logger

class ParserHelper:
    """
    Represents a helper class for Parser
        currencies_file = a file containing currency symbols 
            and corresponding codes (1:N)
    """
    def __init__(self, currencies_file='currency_symbols.json'):
        self.currencies_file = currencies_file

    def is_currency_code(self, input_string):
        input_string = input_string.strip()

        # Check format - 3 capital letters
        pattern = re.compile(r'\s*[A-Z]{3}\s*')
        if pattern.match(input_string):
            # Check the code against codes in the file
            with open(self.currencies_file) as file:
                currencies = json.load(file)
                # 1 symbol can have more currency codes
                for currency_codes in currencies.values():
                    if input_string in currency_codes:
                        return True
        return False

    def is_currency_symbol(self, input_string):
        input_symbol = input_string.strip()
        with open(self.currencies_file) as file:
            currencies = json.load(file)
            if input_symbol.decode('utf-8') in currencies.keys():
                return True
        return False

    def get_currency_from_symbol(self, input_currency):
        with open(self.currencies_file) as file:
            currencies = json.load(file)
            # Get both symbols and corresponding currency codes
            for symbol, codes in currencies.iteritems():
                if input_currency.decode('utf-8') == symbol:
                    # Return the 1st currency code for the given symbol
                    return codes[0]
        # Handle errors
        msg = strings.CODE_FROM_SYMBOL_ERROR
        msg = msg.format(input_currency, self.currencies_file)
        Logger.log_error(msg)
        return None