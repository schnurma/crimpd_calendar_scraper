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
import getpass
import logging
import re
import pytest
from pytest import MonkeyPatch
from project import get_credentials, get_month_year_export, create_csv_file

# https://www.youtube.com/watch?v=ULxMQ57engo&t=1258s

def test_get_credentials(monkeypatch: MonkeyPatch):
    """ Test that the function returns a tuple """
    def mock_input(prompt):
        return "test_username"
    def mock_getpass(prompt):
        return "test_password"

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr(getpass, 'getpass', mock_getpass)

    result = get_credentials()

    assert isinstance(result, tuple)
    assert result[0] == "test_username"
    assert result[1] == "test_password"

class TestGetMonthYearExport():
    """ check if the correct month and year is returned """

    def test_correct_values(self, monkeypatch: MonkeyPatch) -> None:
        """ test correct values"""
        inputs = ["12-2099"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        assert get_month_year_export(input) == ("12-2099")

    def test_error_handling(self, monkeypatch: MonkeyPatch) -> None:
        """ test error handling if not a valid month/year is entered"""
        with pytest.raises(Exception) as err:
            inputs = ["13-2099"]
            monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
            get_month_year_export(input)
        with pytest.raises(Exception) as err:
            inputs = ["22-2099"]
            monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
            get_month_year_export(input)


def test_create_csv_file() -> None:
    """ check if csv file is created with the correct name """
    dict_workouts = { "5" : "Test Workout", "6" : "Test Workout 2" }
    workout_month = "January"
    assert create_csv_file(dict_workouts, workout_month) == ("workout_export_January.csv")
    assert create_csv_file(dict_workouts, workout_month) != ("workout_export_February.csv")

