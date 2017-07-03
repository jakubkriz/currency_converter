#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import re

def currency_type(input_string):
    input_string = input_string.strip()
    error_message = '{0} is not a valid currency code, nor a currency symbol.'.format(input_string)
   
    # 3-letter currency code
    if len(input_string) == 3:
        pattern = re.compile(r'[A-Z]{3}')
        if not pattern.match(input_string):
            raise argparse.ArgumentTypeError(error_message)
    # currency symbol
    else:
        if not is_currency_symbol(input_string):
            raise argparse.ArgumentTypeError(error_message)

    return input_string

def is_currency_symbol(input_string):
    # TODO
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