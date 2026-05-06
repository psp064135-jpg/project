import time
from idlelib.run import quitting

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Set up WebDriver
driver = webdriver.Firefox()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window() #login page
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('Sanadi@123') #enter key
driver.find_element(By.XPATH, "//span[contains(text(), 'Sign In')]").click() #contain(condition)
#click on text
time.sleep(5)
element = driver.find_element(By.XPATH, "//p[normalize-space()='SKD SIRI HRM']")
current_url = driver.current_url
print(current_url)#current url
window_handel = driver.current_window_handle
print(window_handel)#window handeling
size = element.size#window size
print("Width:", size['width'])
print("Height:", size['height'])
#indows = driver.window_handles
#driver.switch_to.window(windows[1])
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.back()#back
driver.close()