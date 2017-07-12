# -*- coding: utf-8 -*-
import os

def_path = os.path.dirname(__file__)

LOG_FILE = os.path.join(def_path, "log.txt") 

# Mapping between currency symbols and currency codes
CURR_SYM_FILE = os.path.join(def_path, "currency_symbols.json")

# List of currencies obtained from the API last time
TEMP_CURR_FILE = os.path.join(def_path, "currencies.txt")