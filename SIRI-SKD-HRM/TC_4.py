import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# for filter button
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
driver.find_element(By.XPATH," //span[normalize-space()='Department']").click()
time.sleep(3)#department name
driver.find_element(By.XPATH, "//th[2]//button//filtericon//*[name()='svg']").click()
time.sleep(3)#filter button
driver.find_element(By.XPATH,"//input[@class='p-inputtext p-component p-element ng-star-inserted']").send_keys('IT')
time.sleep(5)#text field
elements = driver.find_element(By.XPATH,"//span[text()='Apply']").click() #click on text
if elements:
    elements[0].click()
    print("Element with text containing 'IT' is present and clicked.")
else:
    print("Element with text containing 'IT' not found.")
