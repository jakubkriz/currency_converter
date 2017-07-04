# -*- coding: utf-8 -*-

import argparse
import re
import json

class CurrencyConverterHelper:
    """
    Represents a helper class for CurrencyConverter
    """
    @staticmethod
    def is_currency_code(input_string):
        input_string = input_string.strip()

        # Check format - 3 letters in uppercase
        pattern = re.compile(r'\s*[A-Z]{3}\s*')
        if pattern.match(input_string):
            # Check the code against codes in the file
            with open("currency_symbols.json") as file:
                currencies = json.load(file)
                for currency_codes in currencies.values():
                    if input_string in currency_codes:
                        return True
        
        return False

    @staticmethod
    def is_currency_symbol(input_string):
        input_symbol = input_string.strip()
        with open("currency_symbols.json") as file:
            currencies = json.load(file)
            if input_symbol.decode('utf-8') in currencies.keys():
                return True
            else:
                return False