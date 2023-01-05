import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
import helpers.helpers as utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re
#from tests.Config import *
from tests.TestBase import *
from datetime import date

@pytest.mark.smoke
def test_demoBlaze(chrome):
    tc_name = "DemoBlaze"
    try:
        chrome.get("https://www.demoblaze.com/")
        chrome.maximize_window()
        chrome.find_element(By.ID, "login2").click()
        time.sleep(5)
        chrome.find_element(By.ID, "loginusername").click()
        chrome.find_element(By.ID, "loginusername").send_keys("ken_villarruel@sbcglobal.net")
        time.sleep(5)
        chrome.find_element(By.ID, "loginpassword").click()
        chrome.find_element(By.ID, "loginpassword").send_keys("Twinlakes01!")
        time.sleep(5)
        # Submit Button
        chrome.find_element(By.XPATH, "//div[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(5)
        #screenshot("pass", tc_name + "_1")
        # Logout
        chrome.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(5)
        chrome.close()
    except:
        #screenshot("fail", tc_name + "_1")
        chrome.close()
        raise