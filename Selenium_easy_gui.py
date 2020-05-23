import os
import easygui
from easygui import *
import sys
from termcolor import colored
import time
import datetime
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


def Selenium_easygui():
    loop = 0
    while True:
        image = "Selenium.png"
        msg ="********************************************************************************\n\n                        SELENIUM SNAPSHOTS GUI INTERFACE\n           ********************************************************************************\n\n                * THIS PROGRAM WILL TAKE SNAPSHOTS OF THE SITES YOU VISIT\n\n                * THE SELENIUM WEBDRIVER WILL MANAGE THE BROWSER'S\n                  INSTANCES SO THAT YOU CAN TAKE SNAPSHOTS\n\n\n                    ---> YOU CAN USER EITHER FIREFOX OR CHROME"
        title = "SELENIUM SNAPSHOTS"
        choices = [ "Mozilla Firefox Snapshots", "Google Chrome Snapshots", "EXIT PROGRAM"]
        choice = buttonbox(msg ,title, image=image, choices=choices)
        if choice == "Mozilla Firefox Snapshots":
            #driver.get(screenshots_portal)
            driver = webdriver.Firefox()
            #driver = webdriver.Chrome()
            
            loop = 1
            while True:

                image = "snapshot_icon.png"
                snapshot_taken = " "
                msg ="********************************************************************************\n\n                 YOU ARE IN THE MOZILLA FIREFOX SNAPSHOTS SCREEN\n   ********************************************************************************\n\n   ---> THE SNAPSHOTS WILL BE SAVED IN THE Selenium_Snapshots FOLDER\n\n   ---> ONCE YOU TAKE A SNAPSHOT THE SCREEN WILL BLINK ONCE, YOU CAN LOOK AT\n        THE CONSOLE, TO SEE THE SNAPSHOT´S NAME\n\n   ---> TO TAKE A SNAPSHOT OF THE CURRENT SITE PRESS: Take a Snapshot\n\n"
                title = "MOZILLA FIREFOX SNAPSHOTS SCREEN"
                choices = [ "Take a Snapshot", "Terminate Selenium Firefox", "<-- Back to Main Menu", "EXIT PROGRAM"]
                choice = buttonbox(msg ,title, image=image, choices=choices)
                if choice == "Take a Snapshot":
                    Screenshots = os.system('mkdir -p Selenium_Snapshots')
                    pwd = os.system('pwd')
                    #path_to_screenshots = str("Path to the Snapshots folder is: ")+str(pwd)+"/"+str(Screenshots)+"/"
                    now = datetime.now()
                    print("-------------------------------------")
                    space = " "
                    date = "DATE"
                    time = "TIME"
                    day = "dd"
                    month = "mm"
                    year = "yy"
                    dash="/"
                    hour="hh"
                    minute="mm"
                    seconds="ss"
                    dash="-"
                    dd_mm_yy_hh_mm_ss_ms = day + dash + month + dash + year + space + space + space + hour + dash + minute + dash + seconds
                    try:

                        print("Snapshot date and time: \n")
                        print(dd_mm_yy_hh_mm_ss_ms)
                        yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                        hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
                        todayis = (str(yymmday)+"-"+str(hhmmss))
                        print(str(yymmday)+"  "+str(hhmmss)+'\n')
                        snapshot_name = todayis+".png"
                        driver.save_screenshot("selenium_snapshot_"+snapshot_name)
                        print("Snapshot taken: selenium_snapshot_"+snapshot_name)
                        os.system('mv selenium_snapshot* Selenium_Snapshots')
                        print("----------------------------------------------------------")
                        print("Listing the Snapshots taken in Selenium_Snapshots folder:\n")
                        os.system('ls -l -h Selenium_Snapshots/')

                    except:
                        msg = "ERROR: NO SELENIUM FIREFOX INSTANCE RUNNING, PLEASE GO TO MAIN MENU\n\n       AND PRESS THE Mozilla Firefox Snapshots BUTTON, TO LAUNCH AN INSTANCE OF\n\n       FIREFOX\n\n\n                   ---> PRESS OK TO GET BACK TO MAIN MENU"
                        title = "ERROR MESSAGE - NO FIREFOX INSTANCE RUNNING"
                        redcross = 'redcross.png'
                        msgbox(msg, title, image=redcross)
                    

                if choice == "Terminate Selenium Firefox":
                    driver.quit()
                    broken_firefox = 'broken_firefox.png'
                    msg = "NOTE: YOU HAVE TERMINATED ALL THE SELENIUM FIREFOX INSTANCES\n\n\n                   ---> PRESS OK TO CONTINUE"
                    title = "SELENIUM FIREFOX INSTANCE TERMINATED"
                    msgbox(msg, title, image=broken_firefox)

                if choice == "<-- Back to Main Menu":
                    Selenium_easygui()

                if choice == "EXIT PROGRAM":
                    image = "warning.png"
                    msg = "Do you want to Quit the Program?"
                    title = "Quit Program?"
                    choices = ["Yes", "No"]
                    choice = buttonbox(msg, title, choices, image=image)
                    if choice == "Yes":
                        sys.exit(0)
                    if choice == "No":
                        loop = 1

        if choice == "Google Chrome Snapshots":
            driver = webdriver.Chrome()
            
            loop = 1
            while True:

                image = "snapshot_icon.png"
                msg ="********************************************************************************\n\n                 YOU ARE IN THE GOOGLE CHROME SNAPSHOTS SCREEN\n   ********************************************************************************\n\n   ---> THE SNAPSHOTS WILL BE SAVED IN THE Selenium_Snapshots FOLDER\n\n   ---> ONCE YOU TAKE A SNAPSHOT THE SCREEN WILL BLINK ONCE, YOU CAN LOOK AT\n        THE CONSOLE, TO SEE THE SNAPSHOT´S NAME\n\n   ---> TO TAKE A SNAPSHOT OF THE CURRENT SITE PRESS: Take a Snapshot\n\n"
                title = "GOOGLE CHROME SNAPSHOTS SCREEN"
                choices = [ "Take a Snapshot", "Terminate Selenium Chrome", "<-- Back to Main Menu", "EXIT PROGRAM"]
                choice = buttonbox(msg ,title, image=image, choices=choices)
                if choice == "Take a Snapshot":
                    try:

                        Screenshots = os.system('mkdir -p Selenium_Snapshots')
                        pwd = os.system('pwd')
                        #path_to_screenshots = str("Path to the Snapshots folder is: ")+str(pwd)+"/"+str(Screenshots)+"/"
                        now = datetime.now()
                        print("-------------------------------------")
                        space = " "
                        date = "DATE"
                        time = "TIME"
                        day = "dd"
                        month = "mm"
                        year = "yy"
                        dash="/"
                        hour="hh"
                        minute="mm"
                        seconds="ss"
                        dash="-"
                        dd_mm_yy_hh_mm_ss_ms = day + dash + month + dash + year + space + space + space + hour + dash + minute + dash + seconds
                        print("Snapshot date and time: \n")
                        print(dd_mm_yy_hh_mm_ss_ms)
                        yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                        hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
                        todayis = (str(yymmday)+"-"+str(hhmmss))
                        print(str(yymmday)+"  "+str(hhmmss)+'\n')
                        snapshot_name = todayis+".png"
                        driver.save_screenshot("selenium_snapshot_"+snapshot_name)
                        print("Snapshot taken: selenium_snapshot_"+snapshot_name)
                        os.system('mv selenium_snapshot* Selenium_Snapshots')
                        print("----------------------------------------------------------")
                        print("Listing the Snapshots taken in Selenium_Snapshots folder:\n")
                        os.system('ls -l -h Selenium_Snapshots/')

                    except:

                        msg = "ERROR: NO SELENIUM CHROME INSTANCE RUNNING, PLEASE GO TO MAIN MENU\n\n       AND PRESS THE Google Chrome Snapshots BUTTON, TO LAUNCH AN INSTANCE OF\n\n       CHROME\n\n\n                   ---> PRESS OK TO GET BACK TO MAIN MENU"
                        title = "ERROR MESSAGE - NO CHROME INSTANCE RUNNING"
                        redcross = 'redcross.png'
                        msgbox(msg, title, image=redcross)

                if choice == "Terminate Selenium Chrome":
                    driver.quit()
                    broken_chrome = 'chrome_broken.png'
                    msg = "NOTE: YOU HAVE TERMINATED ALL THE SELENIUM CHROME INSTANCES\n\n\n                   ---> PRESS OK TO CONTINUE"
                    title = "SELENIUM CHROME INSTANCE TERMINATED"
                    msgbox(msg, title, image=broken_chrome)

                if choice == "<-- Back to Main Menu":
                    Selenium_easygui()

                if choice == "EXIT PROGRAM":
                    image = "warning.png"
                    msg = "Do you want to Quit the Program?"
                    title = "Quit Program?"
                    choices = ["Yes", "No"]
                    choice = buttonbox(msg, title, choices, image=image)
                    if choice == "Yes":
                        sys.exit(0)
                    if choice == "No":
                        loop = 1

        if choice == "EXIT PROGRAM":
            image = "warning.png"
            msg = "Do you want to Quit the Program?"
            title = "Quit Program?"
            choices = ["Yes", "No"]
            choice = buttonbox(msg, title, choices, image=image)
            if choice == "Yes":
                sys.exit(0)
            if choice == "No":
                loop = 0
Selenium_easygui()
        
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

def is_alert_present(self):
    try: self.driver.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True

def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally: self.accept_next_alert = True

#def tearDown(self):
    #self.driver.quit()
    #self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
