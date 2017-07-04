# -*- coding: utf-8 -*-

import unittest
import argparse
import strings

from helpers.parser import Parser

class TestParser(unittest.TestCase):
    # def setUp(self):

    def test_currency_type(self):
        # USD must be marked a valid currency type
        input_str = 'USD'
        self.assertTrue(Parser.currency_type(input_str))

        # Dollar sign must be marked a valid currency type
        input_str = '$'
        self.assertTrue(Parser.currency_type(input_str))

        # A valid currency code surrounded by whitespace characters is valid
        input_str = ' GBP   '
        self.assertTrue(Parser.currency_type(input_str))

        # A valid currency symbol must be marked valid
        input_str = 'лв'
        self.assertTrue(Parser.currency_type(input_str))

        # Errors: 
        error_msg = strings.INVALID_INPUT.format(input_str)

        # Numbers are not a valid currency type
        input_str = '123'
        with self.assertRaises(argparse.ArgumentTypeError) as ctxt:
            Parser.currency_type(input_str)
            self.assertTrue(error_msg in ctxt.exception)

        # Random characters are not a valid currency type either
        input_str = 'aBsij'
        with self.assertRaises(argparse.ArgumentTypeError) as ctxt:
            Parser.currency_type(input_str)
            self.assertTrue(error_msg in ctxt.exception)

        # Invalid currency code is not a valid currency type
        input_str = 'AAA'
        with self.assertRaises(argparse.ArgumentTypeError) as ctxt:
            Parser.currency_type(input_str)
            self.assertTrue(error_msg in ctxt.exception)

        # Invalid currency symbol is not a valid currency type as well
        input_str = '@'
        with self.assertRaises(argparse.ArgumentTypeError) as ctxt:
            Parser.currency_type(input_str)
            self.assertTrue(error_msg in ctxt.exception)

    # def tearDown(self):

