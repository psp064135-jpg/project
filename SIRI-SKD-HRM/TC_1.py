import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Set up WebDriver

driver.find_element(By.CSS_SELECTOR, ".p-element.primary.p-button.p-component.ng-star-inserted").click()#new button
time.sleep(3) #css selector= driver.element(By.CSS_SELECTOR,".class name")

driver.find_element(By.XPATH,"//input[@id='department_name']").send_keys('department-152')
time.sleep(3) #department name
driver.find_element(By.XPATH,"//span[text()='Save']").click() # save button
time.sleep(3) #save make sure there is no spaces in css use dot btwn them

driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/div[1]/button[1]/span[1]").click()
time.sleep(3) #for edit button relative X path

driver.find_element(By.XPATH,"//input[@id='department_name']").clear() #clear
driver.find_element(By.XPATH,"//input[@id='department_name']").send_keys('department-153')
time.sleep(3)
driver.find_element(By.XPATH,"//span[text()='Save']").click()
# save button
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='Inactive']").click()
time.sleep(3) #inactive button
driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/div[1]/button[1]/span[1]").click()
time.sleep(3)#restore button
driver.find_element(By.XPATH,"//span[normalize-space()='Active']").click()
time.sleep(3) #active button
element = driver.find_element(By.XPATH, "//h4[text()='department']")#headding tag
actions = ActionChains(driver)#double click
actions.double_click(element).perform()
time.sleep(5)
driver.quit()
#element = driver.find_element(By.XPATH, "//p[normalize-space()='SKD SIRI HRM']")
# //p[normalize-space()='SKD SIRI HRM']