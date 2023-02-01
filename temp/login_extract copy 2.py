import time
import calendar
import locale
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

# for German locale
# check locale -a for available locales
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

USR_NAME = "champion-x@web.de"
USR_PW = "6!=145_crimpd"

# Create the service
service = Service('/usr/local/bin/chromedriver')
# Start the service
service.start()
# Create the driver
driver = webdriver.Remote(service.service_url)

# Navigate to the URL
#driver.get("https://my.crimpd.com/workouts")
driver.get("https://my.crimpd.com/login")

print("find Username field")
# Wait for the login form to become available
username_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(1)"))
)

#/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/ion-list/ion-item[1]/ion-input
# Enter the username
if driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(1)"):
    username_field = driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(1)")
    username_field.send_keys(USR_NAME)
    print("found username field")
    
# Enter the password
#password_field = driver.find_element_by_name("password")
if driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(2)"):
    password_field = driver.find_element(By.CSS_SELECTOR, "ion-item.item-interactive:nth-child(2)")
    password_field.send_keys(USR_PW)
    print("found password field")

time.sleep(1)
# Submit the form
# CSS_SELECTOR
# .form-large > loading-button:nth-child(3)
# XPATH
#/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/loading-button
if driver.find_element(By.XPATH, "/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/loading-button"):
     # seconds
    driver.find_element(By.XPATH, "/html/body/app-root/ion-app/ion-router-outlet/page-login/ion-content/div[2]/div[2]/div/form/loading-button").click()
    print("found login button")

# wait for the page to load
time.sleep(5)

# Switch to the Training History page
driver.get("https://my.crimpd.com/calendar")

# Shold be years, year, month, day, days, workout...
#data_dict = {year: "", month: "", day: "", workout: ""}
data_dict =  {"days" : { "day" : { "workout" : ""}}}

time.sleep(2)
# Wait for the Training History link to become available
#https://my.crimpd.com/calendar
#.page-title > span:nth-child(1)
training_history_link = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title > span:nth-child(1)")))

# Request the current month
now = datetime.now()
print("Datetime: ", now)
current_month = now.strftime("%B")

# Get Month Name
#.monthName
elements = driver.find_element(By.CSS_SELECTOR, ".monthName")
calendar_date = elements.text
calendar_month = calendar_date.split(" ")[0]
print(calendar_date, calendar_month, current_month)
# Check if the current month is the same as the calendar month
# Click on button for last month
#.navigateMonthsBar > ion-button:nth-child(1)
if calendar_month == current_month:
    print("Month is the same")
    driver.find_element(By.CSS_SELECTOR, ".navigateMonthsBar > ion-button:nth-child(1)").click()
    print("clicked on last month")
    
elements = driver.find_element(By.CSS_SELECTOR, ".monthName")
print(elements.text)

# Get the days
# dayNumber

elements = driver.find_elements(By.CLASS_NAME, "day-inner")
#elements = driver.find_elements(By.CSS_SELECTOR, "div.week:nth-child(3) > div:nth-child(1)")
#div.week:nth-child(3) > div:nth-child(2)
#div.week:nth-child(3) > div:nth-child(6)
#elements = driver.find_elements(By.CLASS_NAME, "dayWrap ng-star-inserted")
# css selctor each tile = div.week:nth-child(3) > div:nth-child(1)
# or class name = dayWrap ng-star-inserted
# tile class = day-inner
# day = dayNumber
# day of this month = day passed
# weekend day of this month = day weekendDay passed
for element in elements:
    element1 = element.find_element(By.CLASS_NAME, "dayNumber")
    print(element1.text)
    try:
        element2 = element.find_elements(By.TAG_NAME, "span")
        for element3 in element2:
            print(element3.text)
    except NoSuchElementException:
        print("No workout for this day")
# Get the workouts for each day
    #for element2 in elements2:
     #   print(element2.text)

"""
for element in elements:
    # check if the day is in the current month
    try:
        element1 = element.find_element(By.CLASS_NAME, "day differentMonth passed")
        print("Day is not in the current month")
    except NoSuchElementException:
        print("Day is in the current month")
        # check if the day is a weekend day
    try:
        element1 = element.find_element(By.CLASS_NAME, "day passed]")
        print("Day is from this month")
            #print(element1.text)
    except NoSuchElementException:
        print("Day Error")
    try:
        element1 = element.find_element(By.CLASS_NAME, "day weekendDay passed")
        print("Day is a weekend day")
    except NoSuchElementException:
        print("Day is not a weekend day")

    element1 = element.find_element(By.CLASS_NAME, "dayNumber")
    print(element1.text)
    try:
        element2 = element.find_elements(By.TAG_NAME, "span")
        for element3 in element2:
            print(element3.text)
    except NoSuchElementException:
        print("No workout for this day")
"""

print("done")
# Close the WebDriver instance
driver.quit()
