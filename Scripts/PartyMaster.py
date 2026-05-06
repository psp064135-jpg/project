import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Functions')))
from login import login
from Functions import dropdown
from dropdown import select_dropdown_option
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils
from Functions.Delete_export import delete_and_export
driver = login()
driver.find_element(By.XPATH, "//span[text()='Master']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='Party Master']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='+ Add New']").click()
time.sleep(3)

#import value from xl
file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet  = "PartyMaster"
value  = XLUtils.readData(file, sheet, 2, 1)  # 2nd row, 2nd column
value1 = XLUtils.readData(file, sheet, 2, 2)  # 2nd row, 1st column
value2 = XLUtils.readData(file, sheet, 2, 3)  # 2nd row, 2nd column
value3 = XLUtils.readData(file, sheet, 2, 4)  # 2nd row, 3st column
value4 = XLUtils.readData(file, sheet, 2, 5)  # 2nd row, 4nd column
value5 = XLUtils.readData(file, sheet, 2, 6)  # 2nd row, 1st column

driver.find_element(By.XPATH,"//input[@id='party_name']").send_keys(value)
time.sleep(3)
#dropdown
dropdown_csspath = "div[id='Party Type'] div[aria-label='dropdown trigger']"
option_xpath = "//div[@class='p-element elipsis'][normalize-space()='Supplier']"
select_dropdown_option(driver, dropdown_csspath,option_xpath)
dropdown_csspath = "div[id='Industry Type'] div[aria-label='dropdown trigger']"
option_xpath = "//div[@class='p-element elipsis'][normalize-space()='Sales & Service']"
select_dropdown_option(driver, dropdown_csspath,option_xpath)
dropdown_csspath = "div[id='Region'] div[aria-label='dropdown trigger']"
option_xpath = "//li[@id='Region_0']"
select_dropdown_option(driver, dropdown_csspath,option_xpath)
dropdown_csspath = "div[id='Currency'] div[aria-label='dropdown trigger']"
option_xpath = "//div[@class='p-element elipsis'][normalize-space()='INR']"
select_dropdown_option(driver, dropdown_csspath,option_xpath)
dropdown_csspath = "div[id='State'] div[aria-label='dropdown trigger']"
option_xpath = "//li[@id='State_3']"
select_dropdown_option(driver, dropdown_csspath,option_xpath)
dropdown_csspath = "div[id='Payment Terms'] div[aria-label='dropdown trigger']"
option_xpath = "//li[@id='Payment Terms_1']"
select_dropdown_option(driver, dropdown_csspath,option_xpath)
dropdown_csspath = "div[id='Payment Method'] div[aria-label='dropdown trigger']"
option_xpath = "//div[@class='p-element elipsis'][normalize-space()='G-pay']"
select_dropdown_option(driver, dropdown_csspath,option_xpath)

time.sleep(3)
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys(value1)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='city']").send_keys(value2)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='zip_code']").send_keys(value3)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys(value4)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='phone_number']").send_keys(value5)
time.sleep(3)
driver.find_element(By.XPATH,"//table-field[1]/div[1]/p-table[1]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[11]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@icon='pi pi-pencil']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[2]/p-celleditor[1]/input[1]").send_keys(value1)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[6]/p-celleditor[1]/input[1]").send_keys(value2)
time.sleep(3)
driver.find_element(By.XPATH,"//tbody/tr[@class='p-element ng-star-inserted']/td[7]/p-celleditor[1]/input[1]").send_keys(value3)
time.sleep(3)
XLUtils.deleteRow(file,sheet, 2)
file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet  = "PartyMaster"

time.sleep(3)
driver.find_element(By.XPATH,"//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/thead[1]/tr[1]/th[7]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@icon='pi pi-pencil']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[2]/p-celleditor[1]/input[1]").send_keys(value)
time.sleep(3)#poc name
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[4]/p-celleditor[1]/input[1]").send_keys(value4)
time.sleep(3)#email
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[5]/p-celleditor[1]/input[1]").send_keys(value5)
time.sleep(3)#phone no
driver.find_element(By.XPATH,"//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"table[id='pn_id_146-table'] span[class='p-button-icon pi pi-plus'] ").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@icon='pi pi-pencil']").click()

sheet1  = "PartyMaster1"
value_1 = XLUtils.readData(file, sheet1, 2, 1)  # 2nd row, 2nd column
value_2 = XLUtils.readData(file, sheet1, 2, 2)  # 2nd row, 1st column
value_3 = XLUtils.readData(file, sheet1, 2, 3)  # 2nd row, 2nd column
value_4 = XLUtils.readData(file, sheet1, 2, 4)  # 2nd row, 3st column
value_5 = XLUtils.readData(file, sheet1, 2, 5)  # 2nd row, 4nd column
value_6 = XLUtils.readData(file, sheet1, 2, 6)  # 2nd row, 1st column
value_7 = XLUtils.readData(file, sheet1, 2, 7)  # 2nd row, 4nd column
value_8 = XLUtils.readData(file, sheet1, 2, 8)  # 2nd row, 1st column

time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[2]/p-celleditor[1]/input[1]").send_keys(value_1)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[3]/p-celleditor[1]/input[1]").send_keys(value_2)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[4]/p-celleditor[1]/input[1]").send_keys(value_3)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[5]/p-celleditor[1]/input[1]").send_keys(value_4)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[6]/p-celleditor[1]/textarea[1]").send_keys(value_5)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[7]/p-celleditor[1]/input[1]").send_keys(value_6)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[8]/p-celleditor[1]/input[1]").send_keys(value_7)
time.sleep(3)
driver.find_element(By.XPATH,"//table[1]/tbody[1]/tr[1]/td[9]/p-celleditor[1]/input[1]").send_keys(value_8)
time.sleep(300)
driver.find_element(By.XPATH,"").send_keys()
time.sleep(3)
# delete_and_export(driver)
#
# time.sleep(4)






