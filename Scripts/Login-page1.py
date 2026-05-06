from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils

#testing the login page with xl

driver = webdriver.Chrome()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window()

file="C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"

row = XLUtils.getRowCount(file, "Sheet1")

for r in range(2, row + 1):
     val = XLUtils.readdata(file, "Sheet1", r, 2)
     val1 = XLUtils.readdata(file, "Sheet1", r, 2)

driver.find_element(By.XPATH, "//input[@id='email']").send_keys(val)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(val1)
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Sign In']").click()

driver.save_screenshot("before_login.png")

time.sleep(300)





