#Sub Category Master by taking the data from xl even for search field also,
#taking the category master data from xl
#creating the function for they login credientials
#working
#employee
import sys
import os
# Add the 'Functions' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Functions')))
from login import login  # Now this will work
from Functions.dropdown import select_option
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils
driver = login()  # This launches browser and logs in

driver.find_element(By.XPATH, "//span[text()='Master']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Employee']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)

file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet = "Employee"
sheet1 = "Employe"
# Read values from Excel
value1 = XLUtils.readData(file, sheet, 2, 1)  # 2nd row, 1st column
value2 = XLUtils.readData(file, sheet, 2, 2)  # 2nd row, 2nd column
value3 = XLUtils.readData(file, sheet, 2, 3)  # 2nd row, 3st column
value4 = XLUtils.readData(file, sheet, 2, 4)  # 2nd row, 4nd column
value5 = XLUtils.readData(file, sheet1, 2, 1)  # 2nd row, 1st column
value6 = XLUtils.readData(file, sheet1, 2, 2)  # 2nd row, 2nd column
value7 = XLUtils.readData(file, sheet1, 2, 3)  # 2nd row, 3st column
value8 = XLUtils.readData(file, sheet1, 2, 4)  # 2nd row, 4nd column

#basic details exported from xl
driver.find_element(By.XPATH, "//input[@id='employee_name']").send_keys(value5)
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys(value6)
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='phone_no']").send_keys(value8)
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-inputswitch p-component']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='System Access Group']//div[@aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='MANAGER']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys(value7)


# Call your reusable function
driver.find_element(By.XPATH, "//div[@id='Department']//div[@aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(value1)
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Department 2']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//div[@id='Designation']//div[@aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(value2)
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='des__2']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//div[@id='First Reporting Authority']//div[@aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(value3)
time.sleep(2)
# driver.find_element(By.XPATH, "").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='Second Report Authority']//div[@aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(value4)
time.sleep(2)
driver.find_element(By.XPATH, "//li[@id='Second Report Authority_0']").click()


driver.find_element(By.XPATH, "//div[@class='flex flex-row justify-content-between align-items-center']//div//button[@class='p-element primary p-button p-component ng-star-inserted']").click()
XLUtils.deleteRow(file,sheet1, 2) # Delete the 2nd row

time.sleep(200)


