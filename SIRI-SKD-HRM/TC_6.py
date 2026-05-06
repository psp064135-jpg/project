
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# edit, active, inactive for the employee details
# Set up WebDriver
driver = webdriver.Chrome()
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
driver.find_element(By.XPATH," //span[normalize-space()='Employee']").click()
time.sleep(3)#grade name

#driver.find_element(By.XPATH,"").click()
#time.sleep(3) #


#editing of the employee details
driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/div[1]/button[1]").click()
time.sleep(3)#edit button
driver.find_element(By.XPATH,"//input[@id='first_name']").click()
time.sleep(3) #click on employee text
driver.find_element(By.XPATH, "//input[@id='first_name']").clear()
time.sleep(3) #clear field of name
driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys('yashwantha')
time.sleep(3) #new name
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(5) #save button

#inactive
driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/div[1]/button[2]").click()
time.sleep(6) #delete button
driver.find_element(By.XPATH,"//button[@aria-label='Yes']").click()
time.sleep(6) #yes button
driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/div[1]/button[2]").click()
time.sleep(6) #delete button
driver.find_element(By.XPATH,"//button[@aria-label='Yes']").click()
time.sleep(6) #yes button
driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/div[1]/button[2]").click()
time.sleep(6) #delete button
driver.find_element(By.XPATH,"//button[@aria-label='Yes']").click()
time.sleep(6) #yes button
driver.find_element(By.XPATH,"//span[normalize-space()='Inactive']").click()
time.sleep(3) #inactive button
driver.find_element(By.XPATH,"//input[@placeholder='Search keyword']").send_keys('yas')
time.sleep(3) #search button
driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/div[1]/button[1]/span[1]").click()
time.sleep(3) #restore button
driver.find_element(By.XPATH,"//button[@label='Active']").click()
time.sleep(3) #active button

