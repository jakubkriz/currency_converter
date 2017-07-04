# -*- coding: utf-8 -*-

import unittest

from helpers.currency_converter_helper import CurrencyConverterHelper

class TestCurrencyConverterHelper(unittest.TestCase):
    # def setUp(self):

    def test_is_currency_code(self): 
        # A valid currency code must be recognized
        currency_code = 'CZK'
        is_curr_code = CurrencyConverterHelper.is_currency_code(currency_code)
        self.assertEqual(is_curr_code, True)

        # A valid currency code can also be surrounded by whitespace characters
        currency_code = '  EUR    '
        is_curr_code = CurrencyConverterHelper.is_currency_code(currency_code)
        self.assertEqual(is_curr_code, True)

        # Number is not a currency code
        currency_code = '123'
        is_curr_code = CurrencyConverterHelper.is_currency_code(currency_code)
        self.assertEqual(is_curr_code, False)

        # Currency code must consist of 3 capital letters
        currency_code = 'CZKs'
        is_curr_code = CurrencyConverterHelper.is_currency_code(currency_code)
        self.assertEqual(is_curr_code, False)

        # Currency code must a valid currency
        currency_code = 'AAA'
        is_curr_code = CurrencyConverterHelper.is_currency_code(currency_code)
        self.assertEqual(is_curr_code, False)

    def test_is_currency_symbol(self):
        # A valid currency symbol must be recognized
        currency_symbol = 'Kč' 
        is_curr_symbol = CurrencyConverterHelper.is_currency_symbol(currency_symbol)
        self.assertEqual(is_curr_symbol, True)

        # A valid currency symbol can also be surrounded by whitespace characters
        currency_symbol = '  € '
        is_curr_symbol = CurrencyConverterHelper.is_currency_symbol(currency_symbol)
        self.assertEqual(is_curr_symbol, True)

        # Vietnamese đồng must be recognized as a valid currency symbol
        currency_symbol = '₫'
        is_curr_symbol = CurrencyConverterHelper.is_currency_symbol(currency_symbol)
        self.assertEqual(is_curr_symbol, True)

        # Numbers are not a valid currency symbol
        currency_symbol = '12'
        is_curr_symbol = CurrencyConverterHelper.is_currency_symbol(currency_symbol)
        self.assertEqual(is_curr_symbol, False)

        # Random characters are not a valid currency symbol
        currency_symbol = 'abSbsas'
        is_curr_symbol = CurrencyConverterHelper.is_currency_symbol(currency_symbol)
        self.assertEqual(is_curr_symbol, False)

        # Number sign is not a valid currency symbol
        currency_symbol = '#'
        is_curr_symbol = CurrencyConverterHelper.is_currency_symbol(currency_symbol)
        self.assertEqual(is_curr_symbol, False)

    # def tearDown(self):

