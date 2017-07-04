#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from helpers.parser import Parser
from conversion_manager import ConversionManager

if __name__ == '__main__':
    parsed_args = Parser.parse_arguments(sys.argv[1:])
    print parsed_args.amount
    print parsed_args.input_currency
    print parsed_args.output_currency
    manager = ConversionManager(parsed_args.amount, parsed_args.input_currency)
