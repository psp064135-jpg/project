# login1.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login2(Module, SubModule):
    driver = webdriver.Chrome()
    driver.get("https://uat-smartlabs.amigo-products.com/app/login")
    driver.maximize_window()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys('admin@mail.com')
    driver.find_element(By.ID, 'password').send_keys('admin@123')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='p-button-label']"))).click()

    # Click menu icon
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='p-element p-ripple p-button p-component p-button-icon-only']"))).click()
    time.sleep(2)

    # Click main module using formatted XPath
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[normalize-space()='{Module}']") )).click()
    time.sleep(2)

    # Click submodule using dynamic XPath SubModule
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[normalize-space()='{SubModule}']") )).click()
    time.sleep(2)

    return driver
