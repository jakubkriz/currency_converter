# -*- coding: utf-8 -*-

import argparse

from parser_helper import ParserHelper
import strings

class Parser(object):
    """
    Represents a helper class for parsing command line arguments
    """
    @staticmethod
    def parse_arguments(args):
        parser = argparse.ArgumentParser()

        # Amount - required
        parser.add_argument(
            '--amount', 
            type=float,
            required=True)

        # Input currency - required
        parser.add_argument(
            '--input_currency', 
            type=Parser.currency_type,
            required=True)

        # Output currency - optional
        parser.add_argument(
            '--output_currency', 
            type=Parser.currency_type)

        return parser.parse_args(args)
        
    @staticmethod
    # Currency type used by the parser to recognize a currency
    def currency_type(input_string):
        input_string = input_string.strip()
        error_message = strings.INVALID_INPUT.format(input_string)
        
        # 3-letter currency code or a currency symbol
        if ParserHelper.is_currency_code(input_string) or \
           ParserHelper.is_currency_symbol(input_string):
            return input_string
        else:
            raise argparse.ArgumentTypeError(error_message)
