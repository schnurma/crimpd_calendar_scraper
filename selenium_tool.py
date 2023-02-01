#!/usr/bin/python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2023 Martin Schnur
#
# SPDX-License-Identifier: MIT

"""
`selenium.py`
================================================================================
Contains the modules for the selenium webdriver

* Author(s): Martin Schnur

Implementation Notes
--------------------

**Software and Dependencies:**

* Linux and Python 3.7.3 or Higher

"""
import time
import calendar
import locale
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

def create_service():
    """ Function for creating the service for the webdriver"""
    # Create the service
    service = Service('/usr/local/bin/chromedriver')
    # Start the service
    service.start()
    # Create the driver
    driver = webdriver.Remote(service.service_url)

    return service, driver

def set_url(service, driver, url) -> None:
    """ Function for setting the url of the webdriver"""
    # Set the url
    driver.get(url)

def scraping_fn(service, driver, username, password) -> None:
    """ Function for scraping the data from the website"""
    
    # Wait for the login form to become available
    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(1)"))
    )

    #/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/ion-list/ion-item[1]/ion-input
    # Enter the username
    if driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(1)"):
        username_field = driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(1)")
        username_field.send_keys(username)
        logging.debug("found username field")
        
    # Enter the password
    #password_field = driver.find_element_by_name("password")
    if driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(2)"):
        password_field = driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(2)")
        password_field.send_keys(password)
        logging.debug("found password field")

    time.sleep(1)
    # Submit the form
    # CSS_SELECTOR
    # .form-large > loading-button:nth-child(3)
    # XPATH
    #/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/loading-button
    if driver.find_element(By.XPATH, "/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/loading-button"):
        # seconds
        driver.find_element(By.XPATH, "/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/loading-button").click()
        logging.debug("found login button")

    # wait for the page to load
    time.sleep(5)

    # Switch to the Training History page
    driver.get("https://my.crimpd.com/calendar")

    time.sleep(2)
    # Wait for the Training History link to become available
    #https://my.crimpd.com/calendar
    #.page-title > span:nth-child(1)
    training_history_link = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title > span:nth-child(1)")))

    # Request the current month
    now = datetime.now()
    logging.debug("Datetime: ", now)
    current_month = now.strftime("%B")

    # Create the dicts for the workouts
    dict_workouts = {}

    # Get Month Name
    #.monthName
    elements = driver.find_element(By.CSS_SELECTOR, ".monthName")
    calendar_date = elements.text
    calendar_month = calendar_date.split(" ")[0]
    logging.debug(calendar_date, calendar_month, current_month)
    # Check if the current month is the same as the calendar month
    # Click on button for last month
    #.navigateMonthsBar > ion-button:nth-child(1)
    if calendar_month == current_month:
        logging.debug("Month is the same")
        driver.find_element(By.CSS_SELECTOR, ".navigateMonthsBar > ion-button:nth-child(1)").click()
        logging.debug("clicked on last month")

    elements = driver.find_element(By.CSS_SELECTOR, ".monthName")
    export_month = elements.text
    logging.debug(elements.text)

    elements = driver.find_elements(By.CLASS_NAME, "day-inner")
    # css selctor each tile = div.week:nth-child(3) > div:nth-child(1)
    # or class name = dayWrap ng-star-inserted
    # tile class = day-inner
    # day = dayNumber
    # day of this month = day passed
    # weekend day of this month = day weekendDay passed

    # prints day and workout if available
    for element in elements:
        element1 = element.find_element(By.CLASS_NAME, "dayNumber")
        logging.debug(element1.text)
        dict_workouts[element1.text] = {}
        try:
            workout_list = []
            element2 = element.find_elements(By.TAG_NAME, "span")
            for element2_2 in element2:
                logging.debug(element2_2.text)
                workout_list.append(element2_2.text) 
        except NoSuchElementException:
            logging.debug("Error")
        dict_workouts[element1.text] = workout_list
    
    logging.warning("done")
    # Close the WebDriver instance
    driver.quit()
    return dict_workouts, export_month
