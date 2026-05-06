import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Functions')))
from login import login
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils
driver = login()

file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet = "TermsAndCondi"
value= XLUtils.readData(file, sheet, 2, 1)  # 2nd row, 1st column
value1= XLUtils.readData(file, sheet, 2, 2)

driver.find_element(By.XPATH, "//span[text()='Master']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Terms And Conditions']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='term']").send_keys(value)
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(value1)
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='flex flex-row justify-content-between align-items-center']//div//button[@class='p-element primary p-button p-component ng-star-inserted']").click()
time.sleep(3)


