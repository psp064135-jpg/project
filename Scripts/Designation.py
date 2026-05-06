#designation with screnshots
import sys
import os
import time
from Functions import XLUtils
from Functions.Check_URL import URLs
from selenium.webdriver.common.by import By
from Functions.Delete_export import delete_and_export
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Functions')))

from login import login
driver = login()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Master']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Designation']").click()
time.sleep(2)



# driver.find_element(By.XPATH,"//span[normalize-space()='+ Add New']").click()
# time.sleep(2)
# #export from xl
# file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
# sheet = "designation"
# # Read values from Excel
# value1 = XLUtils.readData(file, sheet, 2, 1)  # 2nd row, 1st column
#
# driver.find_element(By.XPATH,"//input[@id='designation_name']").send_keys(value1)
# time.sleep(2)
# driver.find_element(By.XPATH,"//div[@class='flex flex-row justify-content-between align-items-center']//div//button[@class='p-element primary p-button p-component ng-star-inserted']").click()
# time.sleep(3)#save
# driver.save_screenshot("screenshot.png")#screenshot
#
# file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
# sheet = "designationn"
# # Read values from Excel
# value2 = XLUtils.readData(file, sheet, 2, 1)  # 2nd row, 1st column
#
# driver.find_element(By.XPATH,"//input[@id='designation_name']").clear()
# driver.find_element(By.XPATH,"//input[@id='designation_name']").send_keys(value2)
# time.sleep(3)
# driver.save_screenshot("screenshot.png")#screenshot
# driver.find_element(By.XPATH,"//div[@class='flex flex-row justify-content-between align-items-center']//div//button[@class='p-element primary p-button p-component ng-star-inserted']").click()
# time.sleep(2)#save
# XLUtils.deleteRow(file,sheet, 2) # Delete the first row (index 2)
#
# driver.find_element(By.XPATH,"//tbody[1]/tr[4]/td[3]/div[1]/button[2]").click()
# time.sleep(2)#//table[1]/tbody[1]/tr[3]/td[3]/div[1]/button[2]/span[1]
# driver.find_element(By.XPATH,"//button[@aria-label='Yes']").click()
# time.sleep(2)
# driver.save_screenshot("delete_designation.png")#screenshot
# time.sleep(2)
# driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[3]/div[1]/button[2]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[@aria-label='Yes']").click()
# time.sleep(2)
# driver.save_screenshot("activate.png")#screenshot
# driver.find_element(By.XPATH,"//button[@label='Inactive']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[@class='p-element p-button-sm p-button-rounded p-button-text p-button p-component p-button-icon-only ng-star-inserted']").click()
# time.sleep(2)
# driver.save_screenshot("inactive.png")#screenshot
# driver.find_element(By.XPATH,"//button[@label='Active']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@placeholder='Search keyword']").send_keys("des")
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[@class='p-element p-button-outlined secondary md:hidden lg:flex xl:flex p-button p-component']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[@icon='pi pi-upload']").click()
# time.sleep(2)

delete_and_export(driver)

URL = "/app/masters/designation"
Form = "Designation"
URLs(driver, URL, Form)

