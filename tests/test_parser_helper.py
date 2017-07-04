# -*- coding: utf-8 -*-

import unittest

from helpers.parser_helper import ParserHelper

class TestParserHelper(unittest.TestCase):
    # def setUp(self):

    def test_is_currency_code(self): 
        # A valid currency code must be recognized
        currency_code = 'CZK'
        is_curr_code = ParserHelper.is_currency_code(currency_code)
        self.assertTrue(is_curr_code)

        # A valid currency code can also be surrounded by whitespace characters
        currency_code = '  EUR    '
        is_curr_code = ParserHelper.is_currency_code(currency_code)
        self.assertTrue(is_curr_code)

        # Number is not a currency code
        currency_code = '123'
        is_curr_code = ParserHelper.is_currency_code(currency_code)
        self.assertFalse(is_curr_code)

        # Currency code must consist of 3 capital letters
        currency_code = 'CZKs'
        is_curr_code = ParserHelper.is_currency_code(currency_code)
        self.assertFalse(is_curr_code)

        # Currency code must a valid currency
        currency_code = 'AAA'
        is_curr_code = ParserHelper.is_currency_code(currency_code)
        self.assertFalse(is_curr_code)

    def test_is_currency_symbol(self):
        # A valid currency symbol must be recognized
        currency_symbol = 'Kč' 
        is_curr_symbol = ParserHelper.is_currency_symbol(currency_symbol)
        self.assertTrue(is_curr_symbol)

        # A valid currency symbol can also be surrounded by whitespace characters
        currency_symbol = '  € '
        is_curr_symbol = ParserHelper.is_currency_symbol(currency_symbol)
        self.assertTrue(is_curr_symbol)

        # Vietnamese đồng must be recognized as a valid currency symbol
        currency_symbol = '₫'
        is_curr_symbol = ParserHelper.is_currency_symbol(currency_symbol)
        self.assertTrue(is_curr_symbol)

        # Numbers are not a valid currency symbol
        currency_symbol = '12'
        is_curr_symbol = ParserHelper.is_currency_symbol(currency_symbol)
        self.assertFalse(is_curr_symbol)

        # Random characters are not a valid currency symbol
        currency_symbol = 'abSbsas'
        is_curr_symbol = ParserHelper.is_currency_symbol(currency_symbol)
        self.assertFalse(is_curr_symbol)

        # Number sign is not a valid currency symbol
        currency_symbol = '#'
        is_curr_symbol = ParserHelper.is_currency_symbol(currency_symbol)
        self.assertFalse(is_curr_symbol)

    # def tearDown(self):

