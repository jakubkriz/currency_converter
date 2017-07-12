# -*- coding: utf-8 -*-
import datetime
import sys

class Logger(object):
    """
    A class to log debug information and errors
    """
    def __init__(self, file_name='log.txt'):
        self.file_name = file_name

    def log_debug(self, text):
        time_stamp = datetime.datetime.now() 
        text_file = open(self.file_name, "a+") 
        text_file.write("\n--------\nLogged at: {:%Y-%m-%d %H:%M:%S}\n".format(time_stamp)) 
        text_file.write("[Debug]: %s"%(text))   
        text_file.close() 

    def log_error(self, text):
        time_stamp = datetime.datetime.now() 
        text_file = open(self.file_name, "a+") 
        text_file.write("\n--------\nLogged at: {:%Y-%m-%d %H:%M:%S}\n".format(time_stamp)) 
        text_file.write("[Error]: %s"%(text))   
        text_file.close() 

