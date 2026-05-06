#product master
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

# from Functions.Delete_export import delete_and_export
# driver = delete_and_export()

driver.find_element(By.XPATH, "//span[text()='Master']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Product Master']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Type']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@id='Type_0']").click()
time.sleep(3)

file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet = "ProductMaster"
# Read values from Excel
value1= XLUtils.readData(file, sheet, 2, 1)  # 2nd row, 1st column
value2= XLUtils.readData(file, sheet, 2, 2)
value3= XLUtils.readData(file, sheet, 2, 3)
value4= XLUtils.readData(file, sheet, 2, 4)
value5= XLUtils.readData(file, sheet, 2, 5)
value6= XLUtils.readData(file, sheet, 2, 6)
value7= XLUtils.readData(file, sheet, 2, 7)
value8= XLUtils.readData(file, sheet, 2, 8)
value9= XLUtils.readData(file, sheet, 2, 9)
value10= XLUtils.readData(file, sheet, 2, 10)

driver.find_element(By.XPATH, "//input[@id='item_name']").send_keys(value1)
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Units']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='tons4']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Category']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Cat-32']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//div[@id='Brand']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='HP']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='model']").send_keys(value2)
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='mrp']").send_keys(value3)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='mrp_disc_sale']").send_keys(value4)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='mrp_disc_wholesale']").send_keys(value5)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='purchase_price']").send_keys(value6)
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='quantity']").send_keys(value7)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='price']").send_keys(value8)
time.sleep(3)
driver.find_element(By.XPATH, "//button[@aria-label='Choose Date']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='p-ripple p-element ng-tns-c1685646730-60 ng-star-inserted'][normalize-space()='28']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='min_stock']").send_keys(value9)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='location']").send_keys(value10)
XLUtils.deleteRow(file,sheet, 2) # Delete the first row (index 2)
time.sleep(3)
# driver.find_element(By.XPATH, "//div[@class='p-dialog-footer ng-tns-c4033847114-31 ng-star-inserted']//div[3]//button[2]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//tbody//button[1]").send_keys(value9)
# time.sleep(3)
# driver.find_element(By.XPATH, " ").send_keys(value9)
# time.sleep(3)
# driver.find_element(By.XPATH, " ").send_keys(value9)
# time.sleep(3)
# driver.find_element(By.XPATH, " ").send_keys(value9)
# time.sleep(3)
# driver.find_element(By.XPATH, " ").send_keys(value9)
# time.sleep(3)
# driver.find_element(By.XPATH, " ").send_keys(value9)
# time.sleep(3)



