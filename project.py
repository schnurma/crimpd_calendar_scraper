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
from bs4 import BeautifulSoup
from pyshadow.main import Shadow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

def import_webdriver() -> None:
    """ Function for importing the webdriver"""
    # https://pypi.org/project/chromedriver-autoinstaller/

    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title

def scrapy_website() -> str:
    """ Function for requesting the website using the scrapy module """

    BASE_URL = "https://www.londonstockexchange.com/news-article/market-news/dividend-declaration/15174450"
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find("span", class_="icon2-endurance type-icon") is not None:
        print ("Login successful")
    else:
        print("Login failed")


def selenium_website() -> str:
    """ Function for requesting the website using the selenium module """

    #BASE_URL = "https://www.londonstockexchange.com/news-article/market-news/dividend-declaration/15174450"
    BASE_URL = "https://my.crimpd.com/workouts"
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    shadow = Shadow(driver)
    z = shadow.chrome_driver.get(BASE_URL)
    #element = shadow.find_element(By.CLASS_NAME, 'md ion-page hydrated')
    element = shadow.find_elements('ion-router-outlet')
    print(element)
    #element1 = element.find_elements(By.TAG_NAME, 'span')
 

def requests_website_find() -> str:
    """ Function for requesting the website using the requests module """

    session = requests.Session()
    

    response = session.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    #if soup.find("span", class_="icon2-endurance type-icon") is not None:
    if soup.find(class_="category-header type-icon") is not None:
        print ("Login successful")
    else:
        print("Login failed")


def requests_website() -> str:
    """ Function for requesting the website using the requests module """

    USERNAME = "champion-x@web.de"
    PASSWORD = "6!=145_crimpd"
    BASE_URL = "https://my.crimpd.com"

    session = requests.Session()
    
    #data = {"account": USERNAME, "password": PASSWORD, "remember": "off"}
    data = {"email": USERNAME, "password": PASSWORD}

    response = session.post(BASE_URL + "/login", data=data)
    
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find("Favorite Workouts") is not None:
        print ("Login successful")
    else:
        print("Login failed")


def main() -> None:
    """ Main function """
    print("Hello World")
    #print(requests_website())
    #print(requests_website_find())
    print(selenium_website())
    #print(import_webdriver())



if __name__ == "__main__":
    main()

