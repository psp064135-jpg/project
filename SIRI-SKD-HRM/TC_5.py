
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# grade master
# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window() #login page
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('Sanadi@123') #enter key
driver.find_element(By.XPATH,"//span[text()='Sign In']").click() #click on text
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='p-button-icon pi pi-bars']").click()
time.sleep(3) #click on menu
driver.find_element(By.XPATH,"//span[text()='Master']").click()
time.sleep(3) #click on button
driver.find_element(By.XPATH," //span[normalize-space()='Grade']").click()
time.sleep(3)#grade name

driver.find_element(By.CSS_SELECTOR, ".p-element.primary.p-button.p-component.ng-star-inserted").click()
time.sleep(3) #new button
driver.find_element(By.XPATH,"//input[@id='grade_code']").send_keys('Grade-222')
time.sleep(3) #grade code
driver.find_element(By.XPATH,"//input[@id='grade_description']").send_keys('grade 222')
time.sleep(3) #grade discription

driver.find_element(By.XPATH, "//button[@aria-label='Choose Date']").click()
time.sleep(10)#attribute of calender
driver.find_element(By.XPATH, "//span[normalize-space()='2026']").click()
time.sleep(3)#selecting 2026 xpath

driver.find_element(By.XPATH,"//input[@name='pf_employee_contribution']").send_keys('10')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='pf_employer_contribution']").send_keys('10')
time.sleep(3)#pf_employer_contribution
driver.find_element(By.XPATH,"//input[@name='esi_employee_share']").send_keys('10')
time.sleep(3) #esi_employee_share
driver.find_element(By.XPATH,"//input[@name='esi_employer_share']").send_keys('10')
time.sleep(3) #esi_employer_share
driver.find_element(By.XPATH,"//input[@name='conveyance_allowance']").send_keys('1000')
time.sleep(3) #conveyance_allowance
driver.find_element(By.XPATH,"//input[@name='children_education_allowance']").send_keys('10000')
time.sleep(3)#children_education_allowance
driver.find_element(By.XPATH,"//input[@name='children_hostel_allowances']").send_keys('10000')
time.sleep(3)#children_hostel_allowances cca
driver.find_element(By.XPATH,"//input[@name='cca']").send_keys('10000')
time.sleep(3)#cca
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/div[1]/button[1]/span[1]").click()
time.sleep(3)  # click on edit button
driver.find_element(By.XPATH,"//input[@inputmode='decimal' and @aria-valuemin='0']").send_keys('12')
time.sleep(3)  # text box
driver.find_element(By.XPATH,"//span[@role='combobox' and @aria-label='No']").click()
time.sleep(5)  # yes/no button
driver.find_element(By.XPATH,"//span[text()='Yes']").click()
time.sleep(3)  # selecting yes
driver.find_element(By.CSS_SELECTOR,".p-button-icon.pi.pi-check").click()
time.sleep(3)  # right button

driver.find_element(By.XPATH,"//tbody[1]/tr[2]/td[5]/div[1]/button[1]/span[1]").click()
time.sleep(3)  # click on edit button  #/tbody[1]/tr[2]/td[5]/div[1]/button[1]/span[1]
driver.find_element(By.XPATH,"//input[@inputmode='decimal' and @aria-valuemin='0']").send_keys('12')
time.sleep(3)  # text box
driver.find_element(By.XPATH,"//span[@role='combobox' and @aria-label='No']").click()
time.sleep(5)  # yes/no button
driver.find_element(By.XPATH, "//span[text()='Yes']").click()
time.sleep(3)  # selecting yes
driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(5) div:nth-child(1) button:nth-child(1) span:nth-child(1)").click()
time.sleep(3)  # right button

driver.find_element(By.XPATH,"//tbody[1]/tr[3]/td[5]/div[1]/button[1]/span[1]").click()
time.sleep(3)  # click on edit button
driver.find_element(By.XPATH,"//input[@inputmode='decimal' and @aria-valuemin='0']").send_keys('12')
time.sleep(3)  # text box
driver.find_element(By.XPATH,"//span[@role='combobox' and @aria-label='No']").click()
time.sleep(5)  # yes/no button
driver.find_element(By.XPATH, "//span[text()='Yes']").click()
time.sleep(3)  # selecting yes
driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(3) td:nth-child(5) div:nth-child(1) button:nth-child(1) span:nth-child(1)").click()
time.sleep(3)  # right button

driver.find_element(By.XPATH,"//thead[1]/tr[1]/th[5]/div[1]/button[1]").click()
time.sleep(3)  # click on create button

driver.find_element(By.XPATH,"//tbody[1]/tr[4]/td[5]/div[1]/button[1]/span[1]").click()
time.sleep(3)  # click on edit
driver.find_element(By.XPATH, "//tbody[1]/tr[4]/td[2]/p-celleditor[1]/input[1]").send_keys("other")
time.sleep(3)  # text field
driver.find_element(By.XPATH,"//input[@inputmode='decimal' and @aria-valuemin='0']").send_keys('12')
time.sleep(3)  # number field
driver.find_element(By.XPATH,"//tbody[1]/tr[4]/td[4]/p-celleditor[1]/p-dropdown[1]/div[1]/span[1]").click()
time.sleep(5)  # yes/no button
driver.find_element(By.XPATH, "//span[text()='Yes']").click()
time.sleep(3)  # selecting yes
driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(3) td:nth-child(5) div:nth-child(1) button:nth-child(1) span:nth-child(1)").click()
time.sleep(3)  # right button
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(3)  # save button




driver.quit()


