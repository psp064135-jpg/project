from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl
#contract register
# Launch browser and login
driver = webdriver.Chrome()
driver.get("https://uat-macdata.amigo-products.com/app/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Sanadi@123')
driver.find_element(By.XPATH, "//span[text()='Log in']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Sales & Marketing']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Contact Register']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Party Name']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Pramod']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Type']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='p-element p-ripple p-button-rounded p-button-text p-button-sm p-button p-component p-button-icon-only ng-star-inserted']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[3]/td[7]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//tbody/tr[@class='p-element ng-star-inserted']/td[2]/p-celleditor[1]/input[1]").send_keys("mahi")
time.sleep(3)#
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[3]/td[5]/p-celleditor[1]/input[1]").send_keys("yas@gmail.com")
time.sleep(3)#
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[3]/td[6]/p-celleditor[1]/input[1]").send_keys(2233442233)
time.sleep(3)

