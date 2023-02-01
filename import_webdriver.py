""" Test ChatGPT """

"""
I want to webscrape the workouts from the following page https://my.crimpd.com/workouts
Help me to write a script in Python


Can you adapt the code to scrape the following content
<span _ngcontent-vot-c155="">Endurance</span>    
    
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create the driver
driver = webdriver.Chrome("usr/local/bin/chromedriver")

# Navigate to the URL
driver.get("https://my.crimpd.com/workouts")

# Wait for the elements to become available
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.title span"))
)

# Get the text of each element
for element in elements:
    text = element.text
    print(text)

# Close the WebDriver instance
driver.quit()
