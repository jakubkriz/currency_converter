# -*- coding: utf-8 -*-
import datetime
import sys

from config import LOG_FILE

class Logger(object):
    """
    A class to log debug information and errors
    """
    @staticmethod
    def log_debug(self, text):
        time_stamp = datetime.datetime.now() 
        text_file = open(LOG_FILE, "a+") 
        text_file.write("\n--------\nLogged at: {:%Y-%m-%d %H:%M:%S}\n".format(time_stamp)) 
        text_file.write("[Debug]: %s"%(text))   
        text_file.close() 

    @staticmethod
    def log_error(self, text):
        time_stamp = datetime.datetime.now() 
        text_file = open(LOG_FILE, "a+") 
        text_file.write("\n--------\nLogged at: {:%Y-%m-%d %H:%M:%S}\n".format(time_stamp)) 
        text_file.write("[Error]: %s"%(text))   
        text_file.close() 

