import urllib
import pyautogui
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re
import datetime

def selectBrowser(self, browser):
    if browser == "CHROME":
        self.driver = webdriver.Chrome(executable_path='C:\Wdrivers\chromedriver.exe')
    if browser == "EDGE":
        self.driver = webdriver.Edge(executable_path='C:\Wdrivers\msedgedriver.exe')
    if browser == "FIREFOX":
        self.driver = webdriver.Firefox(executable_path='C:\Wdrivers\geckodriver.exe')
    if browser == "IE":
        options = webdriver.IeOptions()
        options.file_upload_dialog_timeout = 2000
        options.native_events = False
        options.ignore_protected_mode_settings = True
        options.ignore_zoom_level = True
        options.add_argument('-private')
        self.driver = webdriver.Ie(options=options, executable_path='C:\Wdrivers\IEDriverServer.exe')
    return self

def checkurl(portal):
    try:
        status_code = urllib.request.urlopen(portal).getcode()
        #request_response = requests.head(portal, allow_redirects=True)
        #status_code = request_response.status_code
        website_is_up = status_code == 200
        print(status_code)
    except urllib.error.URLError as e:
        print(e.reason)
        if e.reason == "Unauthorized":
            status_code = 200
        else:
            status_code = e.reason

    return status_code

def screenshot(result, tc_name):
    myScreenshot = pyautogui.screenshot()
    if result == "pass":
        screenshot_name = "PASSED" + "_" + tc_name + ".png"
    else:
        screenshot_name = "FAILED" + "_" + tc_name + ".png"
    #screenshot_path = r'C:\CRDLogs\'' + screenshot_name
    screenshot_path = "..\\Logs\\" + screenshot_name
    myScreenshot.save(screenshot_path)


