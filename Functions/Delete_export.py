#active and inactive reuseable methods
from selenium.webdriver.common.by import By
import time

def delete_and_export(driver):
    driver.find_element(By.CSS_SELECTOR, ".p-button-icon.pi.pi-trash").click()
    time.sleep(3)#delete the data
    driver.find_element(By.XPATH, "//button[@aria-label='Yes']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@label='Inactive']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button[class='p-element p-button-sm p-button-rounded p-button-text p-button p-component p-button-icon-only ng-star-inserted']").click()
    time.sleep(3)#search
    driver.find_element(By.XPATH, "//button[@label='Active']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@icon='pi pi-upload']").click()
    time.sleep(3)#exporting the data in xl format



