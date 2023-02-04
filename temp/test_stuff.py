import getpass
import logging
import csv
from datetime import datetime
import _strptime
import re

debug_mode = True

""" Function for setting up the logging """
# https://docs.python.org/3/library/logging.html
# set up logging: set level to DEBUG to see all messages
# set up logging: set level to WARNING to only see warnings and errors
if debug_mode:
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Logging is set to DEBUG")
    logging.basicConfig(level=logging.WARNING)
    
while True:
        try:
            export_date = input("Enter month and year to export (e.g. mm-yyyy): ")
            if re.match(r"^(0[1-9]|1[012])-(20[0-9]{2})$", export_date):
                break
        except Exception as err:
            logging.debug("Error: %s" ,err)