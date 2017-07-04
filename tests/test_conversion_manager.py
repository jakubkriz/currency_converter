# -*- coding: utf-8 -*-

import unittest
from mock import patch
import json

from conversion_manager import ConversionManager
from external_services.currency_api import CurrencyApi

class TestConversionManager(unittest.TestCase):

    @patch.object(CurrencyApi, 'get_rate')  
    def test_convert_amount(self, mock_get_rate):
        rate = 26.000
        mock_get_rate.return_value = rate

        conversion_manager = ConversionManager()

        amount = 100.00
        input_currency = 'EUR'
        output_currency = 'CZK'
        output = conversion_manager.convert_amount(
            amount, input_currency, output_currency)

        mock_get_rate.assert_called_with(input_currency, output_currency)

        expected_output_dict = {
            'input': {
                'currency': input_currency, 
                'amount': amount
                }, 
            'output': {
                output_currency: rate * amount
                }
            }
        expected_output = json.dumps(expected_output_dict)
        self.assertEqual(output, expected_output)  

