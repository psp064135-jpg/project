
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Advance
driver = webdriver.Chrome()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window() #login page
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('Sanadi@123') #enter key
driver.find_element(By.XPATH,"//span[text()='Sign In']").click()
time.sleep(3)#click on text
driver.find_element(By.XPATH,"//span[@class='p-button-icon pi pi-bars']").click()
time.sleep(3) #click on menu
driver.find_element(By.XPATH,"//span[text()='HRM']").click()
time.sleep(3) #click on button
driver.find_element(By.XPATH,"//span[normalize-space()='Advance']").click()
time.sleep(3)#grade name
driver.find_element(By.CSS_SELECTOR,".p-element.primary.p-button.p-component.ng-star-inserted").click()
#new button
#driver.find_element(By.XPATH,"").send_keys('')
time.sleep(3)
driver.find_element(By.XPATH,"//div[@id='Employee Code']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Employee-50 | yash | Tester']").click()
time.sleep(3)#options
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[3]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(3)#calender
driver.find_element(By.XPATH,"//span[normalize-space()='20']").click()
time.sleep(3)#month
driver.find_element(By.XPATH,"//div[@id='Advance Type']").click()
time.sleep(3)#advance dropdown
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Salary Advance']").click()
time.sleep(3)#option
driver.find_element(By.XPATH,"//input[@id='advance_amount']").send_keys('50000')
time.sleep(3)#advance amount
driver.find_element(By.XPATH,"//input[@id='deduction_tenure_months']").send_keys('10')
time.sleep(3)#deduction tenure in months
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[10]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(3)#calender
driver.find_element(By.XPATH,"//span[normalize-space()='May']").send_keys('')
time.sleep(3)#loan starting month
driver.find_element(By.XPATH,"//div[@class='flex flex-row justify-content-between align-items-center']//div//button[@class='p-element primary p-button p-component ng-star-inserted']").click()
time.sleep(600)#save button

