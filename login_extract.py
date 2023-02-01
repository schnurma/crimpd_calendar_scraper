import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

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

# Get Month Name
#.monthName
elements = driver.find_element(By.CSS_SELECTOR, ".monthName")
print(elements.text)
# Get the days
elements = driver.find_elements(By.CLASS_NAME, "dayNumber")
for element in elements:
    print(element.text)

# Get the workouts
# elements2 = driver.find_elements(By.CLASS_NAME, "name")
#for element2 in elements2:
#print(element2.text)



print("done")
# Close the WebDriver instance
driver.quit()
