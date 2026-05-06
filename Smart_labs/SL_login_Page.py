#login page for Smart Labs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login():
    driver = webdriver.Chrome()
    driver.get("https://uat-smartlabs.amigo-products.com/app/login")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@mail.com')
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys('admin@123')
    driver.find_element(By.XPATH, "//span[@class='p-button-label']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()
    time.sleep(4)
    return driver

driver = login()
input("Press Enter to close...")



