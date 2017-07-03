#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import re
import json

def currency_type(input_string):
    input_string = input_string.strip()
    error_message = "{0} is not a valid currency code, nor a currency symbol."
    error_message = error_message.format(input_string)
   
    # 3-letter currency code
    pattern = re.compile(r'[A-Z]{3}')
    if not pattern.match(input_string):
        # currency symbol
        if is_currency_symbol(input_string):
            return input_string
        raise argparse.ArgumentTypeError(error_message)
    else:   
        return input_string

def is_currency_symbol(input_string):
    input_symbol = input_string.strip()
    with open("currency_symbols.json") as file:
        currencies = json.load(file)
        if input_symbol.decode('utf-8') in currencies.keys():
            return True
        else:
            return False

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--amount', type=float)
    parser.add_argument('--input_currency', type=currency_type)
    parser.add_argument('--output_currency', type=currency_type)

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    print get_arguments().amount
    print get_arguments().input_currency
    print get_arguments().output_currency