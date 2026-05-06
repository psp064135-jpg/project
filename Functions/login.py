from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login():
    driver = webdriver.Chrome()
    driver.get("")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@sanadi.com')
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Sanadi@123')
    driver.find_element(By.XPATH, "//span[@class='p-button-label']").click()
    time.sleep(2)

    # driver.find_element(By.CSS_SELECTOR, "div[aria-label='dropdown trigger']").click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, "//span[text()='Testing Branch']").click()
    # time.sleep(2)
    driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()
    time.sleep(4


















































    )
    return driver


