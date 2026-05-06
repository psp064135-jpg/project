#active and inactive reuseable methods
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Functions')))
from login import login
from dropdown import select_dropdown_option
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils
driver = login()
# driver.find_element(By.XPATH, "//span[text()='Master']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//span[normalize-space()='Designation']").click()
# time.sleep(3)
driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/div[1]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@aria-label='Yes']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Inactive']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Active']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@icon='pi pi-upload']").click()
time.sleep(3)



