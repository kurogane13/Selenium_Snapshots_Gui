# Selenium Snapshots Gui
Selenium Snapshots GUI program, that takes snapshots with firefox, or chrome browsers.

*NOTE: You can View the GUI screenshots in the Screenshots folder.
----------------------------------------------------------------------------------------------------------------

Selenium Snapshots GUI program - Author: Gustavo Wydler Azuaga - 05/23/2020
----------------------------------------------------------------------------------------------------------------

Program´s Scope:

The program takes snapshots using the selenium webdrivers, to manage both Mozilla Firefox and Google Chrome.

Functionalities:

    - You can user either Mozilla Firefox, or Google Chrome. 
    - Supports running different instances of each browser. 
    - Both browsers can be used at the same time, opening 2 instances of the same program.
    - You can terminate a browser session either for Firefox and/or Chrome
    - Error messages interface with the user, whenever the driver has no instance of a requested browser
    - All snapshots taken appear in the console, with as a .png file, with a string date and time format
    
How to setup and run the program
----------------------------------------------------------------------------------------------------------------

1. Clone or Download the repo (git clone https://github.com/kurogane13/Selenium_Snapshots_Gui.git)

2. Copy the Selenium Webdrivers for firefox and chrome to the /usr/bin path:
   - sudo cp geckodriver /usr/bin
   - sudo cp chromedriver /usr/bin
   
3. Import the following python libraries:
   - import os
   - import easygui
   - from easygui import *
   - import sys
   - import time
   - import datetime
   - from datetime import datetime
   - from selenium import webdriver
   - from selenium.webdriver.common.by import By
   - from selenium.webdriver.common.keys import Keys
   - from selenium.webdriver.support.ui import Select
   - from selenium.common.exceptions import NoSuchElementException
   - from selenium.common.exceptions import NoAlertPresentException
   - from selenium.webdriver.support.ui import WebDriverWait
   - from selenium.webdriver.support import expected_conditions as EC
   - import unittest, time, re
   
4. Once the libraries are imported, copy all the .png (imagefiles), to the path from where you will
   be running the program. Example: If you will run the program from the /home/$USER path, copy them there.
   
5. Finally, to run the program, open a terminal an run: python3.x Selenium_easy_gui.py. You should get the 
   Main screen with the Selenium logo running.

END OF TUTORIAL
----------------------------------------------------------------------------------------------------------------

