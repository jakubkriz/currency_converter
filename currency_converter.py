#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from helpers.parser import Parser
from conversion_manager import ConversionManager

if __name__ == '__main__':
    parsed_args = Parser.parse_arguments(sys.argv[1:])

    manager = ConversionManager(
        parsed_args.amount, 
        parsed_args.input_currency, 
        parsed_args.output_currency)

    print manager.convert_amount()
