from Functions.SL_fn_login import login2
import time
from selenium.webdriver.common.by import By
from Functions.dropdown import select_option
from Functions.dropdown import select_dropdown_option

Module = 'HRM'
SubModule = 'Employee Salary'
driver = login2(Module, SubModule)
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='p-element primary p-button p-component ng-star-inserted']").click()
time.sleep(2)
# dropdown_csspath = "Employee Code"    function is not working
# time.sleep(2)
# search_value = "emp-183"
# time.sleep(2)
# option = "//li[@id='Employee Code_0']"
# select_dropdown_option(driver,dropdown_csspath,option_xpath)
# select_option(driver, search_value, option)
driver.find_element(By.CSS_SELECTOR,"div[id='Employee Code'] div[aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys("emp-188")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Emp-188 | Sales Coordinator Manager1 | Design-331']").click()
driver.find_element(By.XPATH,"//table//tr[1]//td[5]//button").click()
driver.find_element(By.XPATH,"//p-inputnumber[@class='p-element p-inputwrapper ng-pristine ng-valid ng-star-inserted p-inputwrapper-filled ng-touched p-inputwrapper-focus']//input[@role='spinbutton']").send_keys('1000')
time.sleep(2)

