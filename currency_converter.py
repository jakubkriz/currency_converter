#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from currency_converter_helper import CurrencyConverterHelper
import strings

def currency_type(input_string):
    input_string = input_string.strip()
    error_message = strings.INVALID_INPUT.format(input_string)
   
    # 3-letter currency code or a currency symbol
    if CurrencyConverterHelper.is_currency_code(input_string) or \
       CurrencyConverterHelper.is_currency_symbol(input_string):
        return input_string
    else:
        raise argparse.ArgumentTypeError(error_message)

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--amount', 
        type=float,
        default=None)
    parser.add_argument(
        '--input_currency', 
        type=currency_type,
        default=None)
    parser.add_argument(
        '--output_currency', 
        type=currency_type,
        default=None)

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    print get_arguments().amount
    print get_arguments().input_currency
    print get_arguments().output_currency