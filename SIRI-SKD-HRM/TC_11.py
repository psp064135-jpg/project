from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#salary calcuations
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
driver.find_element(By.XPATH,"//span[normalize-space()='Salary Calculation']").click()
time.sleep(3)#grade name
driver.find_element(By.CSS_SELECTOR,".p-element.primary.p-button.p-component.ng-star-inserted").click()
#new button
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[1]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(3)#from date
driver.find_element(By.XPATH,"//span[text()='1']").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[2]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(3)#to date
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[4]/span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='p-multiselect-trigger']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element'][normalize-space()='Test']").click()
time.sleep(3)#option
driver.find_element(By.XPATH,"//div[@class='p-multiselect-trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[4]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[16]/div[1]/button[1]").click()
time.sleep(3)#edit button
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[4]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys('50')
time.sleep(3)#ot
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[4]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[6]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys('5000')
time.sleep(3)#other expencieve
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[4]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys('3000')
time.sleep(3)#other insective
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[4]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[11]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys('7000')
time.sleep(3)#tax
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[4]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[16]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[3]/sanadi-dialog-footer[1]/div[1]/div[3]/button[2]").click()
time.sleep(3)