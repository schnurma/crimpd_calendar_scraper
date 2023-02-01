""" Test ChatGPT """

"""
I want to webscrape the workouts from the following page https://my.crimpd.com/workouts
Help me to write a script in Python


Can you adapt the code to scrape the following content
<span _ngcontent-vot-c155="">Endurance</span>    
    
"""

"""
import requests
from bs4 import BeautifulSoup

URL = "https://my.crimpd.com/workouts"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Find all workout elements on the page
workouts = soup.find_all("div", class_="workout-card")

# Loop through each workout and extract the Endurance value
for workout in workouts:
    endurance = workout.find("span", attrs={"_ngcontent-vot-c155": ""}).text

    print("Endurance:", endurance)
"""
"""
import requests
from bs4 import BeautifulSoup

URL = "https://my.crimpd.com/workouts"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

endurance = soup.find("span", text="Endurance")

print("Endurance:", endurance.text if endurance else "Endurance not found")

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Create the service
service = Service('/usr/local/bin/chromedriver')

# Start the service
service.start()

# Create the driver
driver = webdriver.Remote(service.service_url)

# Navigate to the URL
driver.get("https://my.crimpd.com/workouts")

# Wait for the element to become available
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ion-app/ion-router-outlet/tabs-component/ion-router-outlet/page-homepage/ion-content/ion-grid/div/div/ion-row[1]/ion-col[1]/div[1]/span[2]"))
)

#endurance = driver.find_element_by_xpath('//span[text()="Endurance"]')

#print("Endurance:", endurance.text)


# Get the text of the element
text = element.text
print(text)

# Close the WebDriver instance
driver.quit()
