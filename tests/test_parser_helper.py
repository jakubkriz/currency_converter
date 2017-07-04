# -*- coding: utf-8 -*-

import unittest

from helpers.parser_helper import ParserHelper

class TestParserHelper(unittest.TestCase):
    # def setUp(self):

    def test_is_currency_code(self): 
        # A valid currency code must be recognized
        currency_code = 'CZK'
        self.assertTrue(ParserHelper.is_currency_code(currency_code))

        # A valid currency code can also be surrounded by whitespace characters
        currency_code = '  EUR    '
        self.assertTrue(ParserHelper.is_currency_code(currency_code))

        # Number is not a currency code
        currency_code = '123'
        self.assertFalse(ParserHelper.is_currency_code(currency_code))

        # Currency code must consist of 3 capital letters
        currency_code = 'CZKs'
        self.assertFalse(ParserHelper.is_currency_code(currency_code))

        # Currency code must a valid currency
        currency_code = 'AAA'
        self.assertFalse(ParserHelper.is_currency_code(currency_code))

    def test_is_currency_symbol(self):
        # A valid currency symbol must be recognized
        currency_symbol = 'Kč' 
        self.assertTrue(ParserHelper.is_currency_symbol(currency_symbol))

        # A valid currency symbol can also be surrounded by whitespace characters
        currency_symbol = '  € '
        self.assertTrue(ParserHelper.is_currency_symbol(currency_symbol))

        # Vietnamese đồng must be recognized as a valid currency symbol
        currency_symbol = '₫'
        self.assertTrue(ParserHelper.is_currency_symbol(currency_symbol))

        # Numbers are not a valid currency symbol
        currency_symbol = '12'
        self.assertFalse(ParserHelper.is_currency_symbol(currency_symbol))

        # Random characters are not a valid currency symbol
        currency_symbol = 'abSbsas'
        self.assertFalse(ParserHelper.is_currency_symbol(currency_symbol))

        # Number sign is not a valid currency symbol
        currency_symbol = '#'
        self.assertFalse(ParserHelper.is_currency_symbol(currency_symbol))

    # def tearDown(self):

