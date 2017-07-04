# -*- coding: utf-8 -*-

import argparse

from parser_helper import ParserHelper
import strings

class Parser:
    """
    Represents a helper class for parsing command line arguments
    """

    @staticmethod
    def parse_arguments(args):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--amount', 
            type=float,
            default=None)
        parser.add_argument(
            '--input_currency', 
            type=Parser.currency_type,
            default=None)
        parser.add_argument(
            '--output_currency', 
            type=Parser.currency_type,
            default=None)

        return parser.parse_args(args)
        
    @staticmethod
    def currency_type(input_string):
        input_string = input_string.strip()
        error_message = strings.INVALID_INPUT.format(input_string)
       
        # 3-letter currency code or a currency symbol
        if ParserHelper.is_currency_code(input_string) or \
           ParserHelper.is_currency_symbol(input_string):
            return input_string
        else:
            raise argparse.ArgumentTypeError(error_message)
