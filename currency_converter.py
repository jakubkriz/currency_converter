#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from helpers.parser import Parser

if __name__ == '__main__':
    parsed_args = Parser.parse_arguments(sys.argv[1:])
    print parsed_args.amount
    print parsed_args.input_currency
    print parsed_args.output_currency
