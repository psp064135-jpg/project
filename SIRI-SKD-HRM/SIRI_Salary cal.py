from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# salary calcuations for salary,advance,bonus and gross salary
driver = webdriver.Chrome()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window()

# Login
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Sanadi@123')
driver.find_element(By.XPATH, "//span[text()='Sign In']").click()
time.sleep(3)

# Navigate
driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-bars']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='HRM']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Salary Calculation']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".p-element.primary.p-button.p-component.ng-star-inserted").click()

# Date selection
driver.find_element(By.XPATH, "//p-tabpanel[1]/div[1]/div[1]/div[1]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='1']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//p-tabpanel[1]/div[1]/div[1]/div[2]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[4]/span[1]").click()

# Select "Test" from dropdown
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-multiselect-trigger']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='p-element'][normalize-space()='Test']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-multiselect-trigger']").click()

# Edit row
time.sleep(2)
driver.find_element(By.XPATH, "//tbody[1]/tr[4]/td[16]/div[1]/button[1]").click()

# Get values
gp = int(driver.find_element(By.XPATH, "//tbody[1]/tr[4]/td[13]//input").get_attribute("aria-valuenow"))  # Gross pay
bonus = int(driver.find_element(By.XPATH, "//tbody[1]/tr[4]/td[8]//input").get_attribute("aria-valuenow"))  # Bonus
advance = int(driver.find_element(By.XPATH, "//tbody[1]/tr[4]/td[9]//input").get_attribute("aria-valuenow"))  # Advance
netpay = int(driver.find_element(By.XPATH, "//tbody[1]/tr[4]/td[14]//input").get_attribute("aria-valuenow"))  # Net Pay
deduction = int(driver.find_element(By.XPATH, "//tbody[1]/tr[4]/td[15]//input").get_attribute("aria-valuenow"))  # Deduction

time.sleep(2)

# Salary calculation
expected_net = gp - bonus - advance
if expected_net == 56400:
    print("Salary is correct")
else:
    print("Salary is incorrect")
    driver.quit
# Advance calculation
expected_advance = gp - bonus - 56400
if expected_advance == advance:
    print(" Advance is correct")
else:
    print(" Advance is incorrect")
    driver.quit
# Bonus calculation
expected_bonus = gp - advance - 56400
if expected_bonus == bonus:
    print(" Bonus is correct")
else:
    print(" Bonus is incorrect")
    driver.quit
# Deduction calculation
expected_deduction = gp - netpay
if expected_deduction == deduction:
    print(" Deduction is correct")
else:
    print(" Deduction is incorrect")
    driver.quit