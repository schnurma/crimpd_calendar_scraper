#!/usr/bin/python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2023 Martin Schnur
#
# SPDX-License-Identifier: MIT

"""
`selenium_tool.py`
================================================================================
Contains the modules for the selenium webdriver and the scraper functions.

* Author(s): Martin Schnur

Implementation Notes
--------------------

**Software and Dependencies:**

* Python 3.10.6 or higher
* Google Chrome Browser Version 109.0.5414.119 or higher
* chromedriver-autoinstaller>=0.4.0
* selenium>=4.8.0

"""
import time
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

#logging.basicConfig(level=logging.DEBUG)

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

def scraping_fn(service, driver, username, password, export_date_str) -> tuple:
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

    # Wait for the Training History link to become available
    time.sleep(2)
    #https://my.crimpd.com/calendar
    #.page-title > span:nth-child(1)
    training_history_link = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title > span:nth-child(1)")))

    # Create the dicts for the workouts
    dict_workouts = {}

    # Request the current month
    now = datetime.now()
    logging.debug("Datetime: %s ", now)
    current_month = now.strftime("%B")
    # Convert the dates to compare them
    # Value added by user
    export_date = datetime.strptime(export_date_str, "%m-%Y")
    export_date_yyyy_mm = datetime.strftime(export_date, "%Y-%m")

    while True :
        # Value from web page
        #.monthName = January 2023
        # Check if the current month is the same as the calendar month
        elements = driver.find_element(By.CSS_SELECTOR, ".monthName")
        workout_date_str = elements.text
        workout_date = datetime.strptime(workout_date_str, "%B %Y")
        workout_date_yyyy_mm = datetime.strftime(workout_date, "%Y-%m")
        # Compare dates
        logging.debug("Comparison Date Website %s and requested month %s", workout_date_yyyy_mm, export_date_yyyy_mm)
        if workout_date_yyyy_mm == export_date_yyyy_mm:
            logging.debug("Date is the same as the export date")
            break
        # Click on button for last month
        #.navigateMonthsBar > ion-button:nth-child(1)
        logging.debug("Date is not the same as the export date")
        driver.find_element(By.CSS_SELECTOR, ".navigateMonthsBar > ion-button:nth-child(1)").click()
        logging.debug("clicked on last month")
        time.sleep(2)


    # css selector each tile = div.week:nth-child(3) > div:nth-child(1)
    # or class name = dayWrap ng-star-inserted
    # tile class = day-inner
    # day = dayNumber
    # day of this month = day passed
    # weekend day of this month = day weekendDay passed
    elements = driver.find_elements(By.CLASS_NAME, "day-inner")

    # prints day and workout if available
    day_counter = 1
    for element in elements:
        element1 = element.find_element(By.CLASS_NAME, "dayNumber")
        logging.debug(element1.text)
        logging.debug("Day Counter: %s", day_counter)
        if int(element1.text) == day_counter:
            # convert int to string, add complete date to dict
            date_str = (str(workout_date_yyyy_mm) + "-" + str(day_counter))
            workout_date = datetime.strptime(date_str, "%Y-%m-%d")
            workout_date_yyyy_mm_dd = datetime.strftime(workout_date, "%Y-%m-%d")
            workout_date_day = datetime.strftime(workout_date, "%A")
            workout_date_complete = workout_date_yyyy_mm_dd + " " + workout_date_day
            # add date to dict as key
            dict_workouts[workout_date_complete] = {}
            day_counter += 1
            try:
                workout_list = []
                element2 = element.find_elements(By.TAG_NAME, "span")
                for element2_2 in element2:
                    # Check if the element has any text
                    if element2_2.text != "":
                        logging.debug(element2_2.text)
                        # add workout to list
                        workout_list.append(element2_2.text)
            except NoSuchElementException:
                logging.debug("Error")
                # add list as value to dict
            dict_workouts[workout_date_complete] = workout_list
    logging.debug(dict_workouts)
    logging.warning("Scraping finished")
    # Close the WebDriver instance
    driver.quit()
    return dict_workouts, workout_date_yyyy_mm
