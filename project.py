#!/usr/bin/python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2023 Martin Schnur
#
# SPDX-License-Identifier: MIT

"""
`project.py`
================================================================================
Script to import the calendar from the Climbing Training App Crimpd to a .csv file
for further use.</br>

With the use of different calendars from different apps and programs like Google,
Garmin, etc. I want to create a handy tool for syncing my training data from 
climbing with my google calendar.

As part of my CS50P final project the first step is to create the web scraper cli 
tool to transform the scraped dataset to a readable .csv file to open it with excel.

* Author(s): Martin Schnur

Implementation Notes
--------------------

**Software and Dependencies:**

* Linux and Python 3.7.3 or Higher

"""
# Imports
import os
import logging
import requests
import locale
import calendar
import getpass
from bs4 import BeautifulSoup
from pyshadow.main import Shadow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

import selenium_tool



def set_up_logging(debug_mode) -> None:
    """ Function for setting up the logging """
    # https://docs.python.org/3/library/logging.html
    # set up logging: set level to DEBUG to see all messages
    # set up logging: set level to WARNING to only see warnings and errors
    if debug_mode:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Logging is set to DEBUG")
    logging.basicConfig(level=logging.WARNING)

def import_webdriver() -> None:
    """ Function for importing the webdriver"""
    # https://pypi.org/project/chromedriver-autoinstaller/
    # Check if the current version of chromedriver exists
    # and if it doesn't exist, download it automatically,
    # then add chromedriver to path
    try:
        chromedriver_autoinstaller.install()

    except Exception as err:
        logging.debug("Error: %s" ,err)

def setup_locale(local_value) -> None:
    """ Function for setting up the locale """
    # Set the locale
    # for your location -> browser language
    # check locale -a for available locales
    # German = de_DE.utf8
    try:
        locale.setlocale(locale.LC_ALL, local_value)
        #locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
    except Exception as err:
        logging.debug("Error: %s" ,err)

def get_credentials() -> tuple:
    """ Function for getting the credentials """
    # Get the credentials from the user
    # https://martinheinz.dev/blog/59
    """
    try:
        #username = getpass.getpass(prompt="Enter your username: ")
        username = input("Enter your username or email: ")
    except Exception as err:
        logging.debug("Error: %s" ,err)
    try :
        password = getpass.getpass(prompt="Enter your password: ")
    except Exception as err:
        logging.debug("Error: %s" ,err)
    """
    #print(username, password)
    username = "champion-x@web.de"
    password = "6!=145_crimpd"

    return username, password

def main() -> None:
    """ Main function """

    # Constants for Settings:
    # Set Value to True to show debugging messages
    DEBUG_MODE = True
    # Set Value for your location -> browser language
    LOCALE_VALUE = 'de_DE.utf8'
    # Set URL for the website
    URL = "https://my.crimpd.com/login"


    logging.warning("Starting Initial Setup...")
    set_up_logging(DEBUG_MODE)
    import_webdriver()
    # for your location -> browser language
    # check locale -a for available locales
    setup_locale(LOCALE_VALUE)
    logging.debug("Locale is set to: %s", locale.getlocale())
    # Get the credentials from the user
    username, password = get_credentials()
    logging.debug(username, password)
    # Start the selenium tool
    service, driver = selenium_tool.create_service()
    selenium_tool.set_url(service, driver, URL)
    dict_workouts, workout_month = selenium_tool.scraping_fn(service, driver, username, password)
    # create the csv file
    print(dict_workouts)
    print(workout_month)
    
if __name__ == "__main__":
    main()

