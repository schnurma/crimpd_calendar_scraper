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

time.sleep(5)
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

# Wait for the Training History link to become available
#https://my.crimpd.com/calendar
#.page-title > span:nth-child(1)
driver.implicitly_wait(5) # seconds
training_history_link = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title > span:nth-child(1)"))
)

# Click the Training History link
if training_history_link:
    print("Training History link found")
    print(training_history_link.text)
else:
    print("Training History link not found, user you are logged in?")

# Wait for the Training History page to load
#.page-title > span:nth-child(1)
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="Training History"]'))
)

# Do any additional actions here, such as extracting information from the Training History page
# Get the text of each element
text = elements.text
print(text)

#for element in elements:
#    text = element.text
#    print(text)

# Close the WebDriver instance
driver.quit()

