from selenium.webdriver.common.by import By
import time

def select_dropdown_option(driver, dropdown_csspath,option_xpath ):
    # Click the dropdown
    driver.find_element(By.CSS_SELECTOR, f"div[id= '{dropdown_csspath}' ] div[aria-label='dropdown trigger']" ).click()
    time.sleep(2)  # Wait for options to load

    # Click the option that matches the text
    #option_xpath = f"//li[normalize-space(text())='{search_text}']"
    driver.find_element(By.XPATH, option_xpath).click()
    time.sleep(1)

def select_option(driver, dropdown, search_value, option):
    driver.find_element(By.CSS_SELECTOR, f"div[id= '{dropdown}' ] div[aria-label='dropdown trigger']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(search_value)
    driver.find_element(By.XPATH, option).click()

     # dropdown div[id='Designation'] div[aria-label='dropdown trigger']
    #//input[@role='searchbox']
    #//input[@role='searchbox']
    #//li[@id='First Reporting Authority_0']
    #//div[@class='p-element elipsis'][normalize-space()='Department-3']
    ##Department_0
    #li[id='Designation_2'] div[class='p-element elipsis']
##Designation_0
    #li[id='First Reporting Authority_0'] div[class='p-element elipsis']
    #//div[@class='p-element elipsis'][normalize-space()='Emp-14 | Deepak | Sales Executive']

    return driver