# **crimpd_calendar_scraper**

- [Crimpd Calendar Scraper](#crimpd-calendar-scraper)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Development](#development)
  - [Filestructure](#filestructure)
  - [Licence and Legal Information](#licence-and-legal-information)


## **Overview**
Script to export the training history from the Climbing Training App Crimpd to a .csv file for further use.</br>

With the use of different calendars from different apps and programs like Google, Garmin, etc. I want to create a handy tool for syncing my training data from climbing with my garmin calendar.

As part of my CS50P final project the first step is to create the web scraper 
tool to transform the scraped dataset to a readable .csv file to open it with excel. After that the data has to be prepared to be synced with the garmin calendar.

It is possible to export the data from the Crimpd app to a .csv file, but for the sake of the python learning process I want to create this with a web scraper tool.

## **Requirements**
This script depends on:

* Python 3.10.6 or higher
* Google Chrome Browser Version 109.0.5414.119 or higher
* chromedriver-autoinstaller>=0.4.0
* selenium>=4.8.0

## **Installation**

At the moment, the tool has no installer.</br> 
Run the following command from within the repository to install the needed requirements.
```
pip install -r requirements.txt
```

## **Usage**
To start the tool, execute the project.py file.
```
python3 project.py
```

After the startup, the tools asks the user for the month which will be scraped from the crimpd training history. In the next prompt the user has to add his user credentials. After that the tool opens chrome and scrapes the activities and creates a *.csv file.

![UserInput](graphics/ccs_tool_userinput.png)


## **Development**
As there is a export function available this tool will not be developed further. But the next step is to adopt the generated dataset to import them into the garmin calendar to sync climbing training data will overall training data.

### **Change settings**
In the main function the logging.debug outputs can be enable with settings the variable debug_mode to True!
```
#Set Value to True to show debugging messages</br>
    debug_mode = False
```
## **Filestructure**

Adafruit-Sensor-Integration-Tool
```
├─ LICENSE.md
├─ README.md
├─ graphics
├─ project.py
├─ selenium_tool.py
└─ requirements.txt
```

## **Related Links**

||Topic|
|-|-|
|1|CS50P: [https://cs50.harvard.edu/python/2022/project/](https://cs50.harvard.edu/python/2022/project/)
|2|Final Project Presentation: [temp](temp)

## **Licence and Legal Information**

Please read the [Legal information](LICENSE.md).
