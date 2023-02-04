#!/usr/bin/python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2023 Martin Schnur
#
# SPDX-License-Identifier: MIT

"""
`test_project.py`
================================================================================
UNIT TESTS for project.py

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
import pytest
from project import get_credentials, get_month_year_export

"""
def test_credentials():
    ''' check if credentials are returned '''
    username = "JohnDoe@harvard.edu"
    password = "123456"
    assert get_credentials() == (username, password)
"""

def test_month_year_export():
    """ check if month and year are returned """
    assert get_month_year_export() == ()
    
    
        