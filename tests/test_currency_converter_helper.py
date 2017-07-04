# -*- coding: utf-8 -*-

import unittest

from helpers.currency_converter_helper import CurrencyConverterHelper

class TestCurrencyConverterHelper(unittest.TestCase):
    # def setUp(self):

    def test_is_currency_code(self): 
        currency_code = 'CZK'
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

    # def test_is_currency_symbol(self):     

    # def tearDown(self):

