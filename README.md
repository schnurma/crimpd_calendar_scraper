# **crimpd_calendar_scraper**

- [Adafruit-Sensor-Integration-Tool](#adafruit-sensor-integration-tool)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Development](#development)
      - [Change settings](#change-settings)
      - [Add a platform](#add-a-platform)
      - [Add a ros2 node](#add-a-ros2-node)
  - [Filestructure](#filestructure)
  - [Contribution and Contribution License Agreement](#contribution-and-contribution-license-agreement)
  - [Licence and Legal Information](#licence-and-legal-information)




## **Overview**
Script to import the calendar from the Climbing Training App Crimpd to a .csv file for further use.</br>

With the use of different calendars from different apps and programs like Google, Garmin, etc. I want to create
a handy tool for syncing my training data from climbing with my google calendar.

As part of my CS50P final project the first step is to create the web scraper cli tool to transform the scraped dataset
to a readable .csv file to open it with excel.


*Supported Platforms*
* Siemens SIMATIC IOT2050
* Raspberry Pi 4B</br>

All Blinka-supported SBCs should work as long as they are GNU/Linux based.
</br>To add a platform read the section Development/Settings.

*Info:* 
The Dockerfile Templates, ROS2 Sensor Nodes are stored in a additional repository : Adafruit_ROS2_Sensor_Node_Bundle</br>
To add new Boards or Sensors, see the Documentation.


## **Requirements**
This script depends on:

* Python 3.7 or higher
* GNU/Linux System
* requests==2.28.1
* docker==5.0.3
* rich==10.15.0
* Adafruit-PlatformDetect>=3.30.0
* Adafruit-Blinka>=8.5.0

## **Installation**

At the moment, the tool has no installer.</br> 
Run the following command from within the repository to install the needed requirements.
```
pip install -r requirements.txt
```

## **Usage**
To start the tool, execute the main.py file.
```
python3 main.py
```

After the startup, the tool shows the user the available Adafuit Sensor and ROS2 Sensor Nodes for the detected platform.
The user has to choose which sensor will be installed.

![Startup](docs/graphics/ASIT_Startup_IOT2050.png)

After the installation, the Sensor Menu is shown with all available options for the sensor.

![SensorMenu](docs/graphics/ASIT_sensor_menu_IOT2050-sgp30.png)

As example, the execution of the Adafruit SGP30 Example file:

![RunExample](docs/graphics/ASIT_sensor_menu_IOT2050-sgp30_run_example_code.png)

Proceeding to the Docker/ROS2 Node Menu, it shows the settings for the Dockerfile and if a ROS2 Sensor Node is available for the chosen sensor.

![NodeMenu](docs/graphics/ASIT_node_menu_IOT2050-sgp30.png)

The user can select which example or node file will be used for the Node creation and which Dockerfile Template will be used.
After the Dockerfile is created, the user can edit the created files and create the Docker Image.

![NodeMenuPythonFile](docs/graphics/ASIT_node_menu_IOT2050-sgp30_pythonfile.png)

The needed commands for executing the Docker Image are at the top of the Dockerfile. This Info block should be implemented in every newly added Dockerfile Template!

![Dockerfile](docs/graphics/ASIT_IOT2050-sgp30_dockerfile.png)



## **Development**
Short introduction on how to develop this tool further.

### **Change settings**
The file utilities/config.py stores the global settings for the tool.

STOP_LIBRARY_REFRESH: disables the library download when set to True. It allows the editing of the local repositories.

TIME: Query value for the repositories. If older than the value, the existing repositories are replaced

DEBUG_MODE: Set to True shows all Debugging Messages

TEXT_EDITOR: This allows changing which text editor is used to open files. Python code = subprocess.call is used.

Further, it contains settings and the keyword comparison for the Dockerfile and Docker Image creation and the paths for the repositories or the chosen file names for directories and pathfinding.

![Config](docs/graphics/ASIT_config.png)

### **Add a platform**
Adafruit PlatformDetect is used to detect the used board and compares the board id with the file structure of the created Adafruit_ROS2_Sensor_Node_Bundle.
To integrate a new board into the tool, the correct board id used from PlatformDetect and the correct board_name from the Bundle have to be added to the function def select_board() in the file utilities/platform_detect.py

PlatformDetect board_id: "RASPBERRY_PI_4B"</br>
Adafruit_ROS2_Sensor_Node_Bundle: board_name = "raspi_4b"

![PlatformDetect](docs/graphics/ASIT_platform_detect.png)
### **Add a ros2 node**
To add a platform and/or a ROS2 Sensor Node, the Adafruit_ROS2_Sensor_Node_Bundle Repository has to be extended.
For this, see the Documentation for the Bundle.


## **Filestructure**

Adafruit-Sensor-Integration-Tool
```
├─ LICENSE.md
├─ README.md
├─ README.md.licence
├─ docs/graphics
├─ data
│  ├─ __init__.py
│  ├─ library
│  │  └─ .gitkeep
│  └─ utilities
│     ├─ __init__.py
│     ├─ config.py
│     ├─ docker_factory.py
│     ├─ input_actions.py
│     ├─ lib_factory.py
│     ├─ node_actions.py
│     ├─ node_factory.py
│     ├─ platform_detect.py
│     ├─ sensor_factory.py
│     ├─ tools.py
│     └─ user_input.py
├─ export
│  ├─ nodes
│  │  └─ .gitkeep
│  └─ workspace
│     └─ .gitkeep
├─ main.py
└─ requirements.txt
```

## **Related Links**

||Topic|
|-|-|
|1|SIMATIC meets Linux: [https://github.com/SIMATICmeetsLinux](https://github.com/SIMATICmeetsLinux)
|2|SIMATIC IOT2050 forum: [https://support.industry.siemens.com/tf/ww/en/threads/309](https://support.industry.siemens.com/tf/ww/en/threads/309)|
|3|SIMATIC IOT2050 Getting Started: [https://support.industry.siemens.com/tf/ww/en/posts/238945/](https://support.industry.siemens.com/tf/ww/en/posts/238945/)|
|4|Operating Instructions: [https://support.industry.siemens.com/cs/ww/en/view/109779016](https://support.industry.siemens.com/cs/ww/en/view/109779016)|
|5|Adafruit CP Bundle: [https://github.com/adafruit/Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)
|6|CircuitPython-Overview: [https://learn.adafruit.com/welcome-to-circuitpython/overview](https://learn.adafruit.com/welcome-to-circuitpython/overview)
|7|CircuitPython-Tricks: [https://github.com/todbot/circuitpython-tricks#outputs](https://github.com/todbot/circuitpython-tricks#outputs)

## Contribution and Contribution License Agreement

Thanks for your interest in contributing. Anybody is free to report bugs, unclear Documentation, and other problems regarding this repository in the Issues section or, even better, is free to propose any changes to this repository using Merge Requests. For more information please check the [Contribution License Agreement](docs/Siemens_CLA.pdf).

## **Licence and Legal Information**

Please read the [Legal information](LICENSE.md).
