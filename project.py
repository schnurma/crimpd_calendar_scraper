#!/usr/bin/python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2023 Martin Schnur
#
# SPDX-License-Identifier: MIT

"""
`project.py`
================================================================================
Script to export a chosen month from the Climbing Training App Crimpd to a .csv file
for further use.</br>

With the use of different calendars from different apps and programs like Google,
Garmin, etc. I want to create a handy tool for syncing my training data from 
climbing with my garmin calendar.

As part of my CS50P final project the first step is to create the web scraper 
tool to transform the scraped dataset to a readable .csv file to open it with excel.
After that the data has to be prepared to be synced with the garmin calendar.

It is possible to export the data from the Crimpd app to a .csv file, but for the sake
of the python learning process I want to create this with a web scraper tool.

* Author(s): Martin Schnur

Implementation Notes
--------------------

**Software and Dependencies:**

* Python 3.10.6 or higher
* Google Chrome Browser Version 109.0.5414.119 or higher
* chromedriver-autoinstaller>=0.4.0
* selenium>=4.8.0

"""
# Imports
import logging
import locale
import getpass
import csv
import chromedriver_autoinstaller
import selenium_tool
from datetime import datetime

def set_up_logging(debug_mode: bool) -> None:
    """ Function for setting up the logging """
    # https://docs.python.org/3/library/logging.html
    # set up logging: set level to DEBUG to see all messages
    # set up logging: set level to WARNING to only see warnings and errors
    if debug_mode:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Logging is set to DEBUG")
    else:
        logging.basicConfig(level=logging.WARNING)
        logging.debug("Logging is set to WARNING")

def import_webdriver() -> None:
    """ Function for importing the chrome webdriver"""
    # https://pypi.org/project/chromedriver-autoinstaller/
    # Check if the current version of chromedriver exists
    # and if it doesn't exist, download it automatically,
    # then add chromedriver to path
    try:
        chromedriver_autoinstaller.install()
    except Exception as err:
        logging.debug("Error: %s" ,err)

def setup_locale(local_value: str) -> None:
    """ Function for setting up the locale """
    # Set the locale
    # for your location -> browser language
    # check locale -a for available locales
    # German = de_DE.utf8
    try:
        locale.setlocale(locale.LC_ALL, local_value)
        #locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
    except Exception as err:
        logging.exception("Error: %s" ,err)

def get_credentials() -> tuple:
    """ Function for getting the credentials """
    # Get the credentials from the user
    # https://martinheinz.dev/blog/59
    username = input("Enter your username or email: ")
    password = getpass.getpass(prompt="Enter your password: ")
    return username, password

def get_month_year_export(input_func=input) -> str:
    """ Ask the user for the month and year to export """
    while True:
        try:
            date_input = input_func("Enter month and year to export (mm-yyyy): ")
            date = datetime.strptime(date_input, "%m-%Y")
            date_mm_yyyy = date.strftime("%m-%Y")
            return str(date_mm_yyyy)
        except ValueError:
            print("Incorrect date format. Please try again.")

def create_csv_file(dict_workouts: dict, workout_month: str) -> None:
    """ Function for creating the csv file """
    # only write days with workouts to the csv file
    # create the csv file
    csv_file = "workout_export_" + workout_month + ".csv"
    with open(csv_file, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Workout"])
        for key, value in dict_workouts.items():
            if value:
                writer.writerow([key, value])
            else:
                logging.debug("No workout for day %s", key)
    return csv_file

def main() -> None:
    """ Main function """
    # Constants for Settings:
    # Set Value to True to show debugging messages
    debug_mode = False
    # Set Value for your location -> browser language
    local_value = 'de_DE.utf8'
    # Set URL for the website
    url = "https://my.crimpd.com/login"

    logging.warning("Starting Initial Setup...")
    set_up_logging(debug_mode)
    import_webdriver()
    # for your location -> browser language
    # check locale -a for available locales
    setup_locale(local_value)
    logging.debug("Locale is set to: %s", locale.getlocale())
    # Get the month and year to export
    export_date  = get_month_year_export(input)
    logging.debug(export_date)
    # Get the credentials from the user
    username, password = get_credentials()
    logging.debug(username, password)
    # Start the selenium tool
    logging.warning("Starting the Browser to scrape the data.")
    service, driver = selenium_tool.create_service()
    selenium_tool.set_url(service, driver, url)
    dict_workouts, workout_month = selenium_tool.scraping_fn(service, driver, username, password, export_date)

    # create the csv file
    csv_file = create_csv_file(dict_workouts, workout_month)
    logging.warning("CSV File created %s", csv_file)

if __name__ == "__main__":
    main()
