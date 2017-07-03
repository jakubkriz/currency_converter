#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--amount', type=float)
    parser.add_argument('--input_currency')
    parser.add_argument('--output_currency')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    print get_arguments()