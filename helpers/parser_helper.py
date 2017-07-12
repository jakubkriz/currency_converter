# -*- coding: utf-8 -*-

import argparse
import re
import json

from logger import Logger
from config import CURR_SYM_FILE

class ParserHelper(object):
    """
    Represents a helper class for Parser
    """
    @staticmethod
    def is_currency_code(input_string):
        input_string = input_string.strip()

        # Check format - 3 capital letters
        pattern = re.compile(r'\s*[A-Z]{3}\s*')
        if pattern.match(input_string):
            # Check the code against codes in the file
            with open(CURR_SYM_FILE) as file:
                currencies = json.load(file)
                # 1 symbol can have more currency codes
                for currency_codes in currencies.values():
                    if input_string in currency_codes:
                        return True
        return False

    @staticmethod
    def is_currency_symbol(input_string):
        input_symbol = input_string.strip()
        with open(CURR_SYM_FILE) as file:
            currencies = json.load(file)
            if input_symbol.decode('utf-8') in currencies.keys():
                return True
        return False

    @staticmethod
    def get_currency_from_symbol(input_currency):
        with open(CURR_SYM_FILE) as file:
            currencies = json.load(file)
            # Get both symbols and corresponding currency codes
            for symbol, codes in currencies.iteritems():
                if input_currency.decode('utf-8') == symbol:
                    # Return the 1st currency code for the given symbol
                    return codes[0]
        # Handle errors
        msg = strings.CODE_FROM_SYMBOL_ERROR
        msg = msg.format(input_currency, CURR_SYM_FILE)
        Logger.log_error(msg)
        return None