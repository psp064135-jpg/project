#employee applying all the reuseable methods
from Functions.login1 import login1
import time
from selenium.webdriver.common.by import By
from Functions.dropdown import select_option
from Functions.Check_URL import URLs
from Functions.Delete_export import delete_and_export
Module = 'Master'
SubModule = 'Employee'
driver = login1(Module, SubModule)
time.sleep(2)

driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(2)
dropdown = "Department"
time.sleep(2)
search_value = "Department"
time.sleep(2)
option = "//div[@class='p-element elipsis'][normalize-space()='Department-3']"
select_option(driver, dropdown, search_value, option)
time.sleep(5)

URL = "/app/masters/employee"
Form = "employee"
URLs(driver, URL, Form)
