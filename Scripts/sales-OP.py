from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils
#macdata sales order profile calcuation, read and write from xls
#check -ve value is occuring
file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet_read = "Sheet3"
sheet_write = "Sheet4"
# Launch browser and login
driver = webdriver.Chrome()
driver.get("https://uat-macdata.amigo-products.com/app/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Sanadi@123')
driver.find_element(By.XPATH, "//span[text()='Log in']").click()
time.sleep(3)
# Navigate to Sales Order Processing
driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Sales & Marketing']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Sales Order Processing']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
# Select dropdowns
driver.find_element(By.XPATH, "//div[@id='Order Processing Type']//div[@aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@id='Order Processing Type_1']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='Customer']//div[@aria-label='dropdown trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/p-scroller/div/ul/p-dropdownitem/li/div/div").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Add Product']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-checkbox-box p-component']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='p-element p-ripple p-button-success p-button-sm p-button p-component ng-star-inserted']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@icon='pi pi-pencil']").click()
time.sleep(3)

# Get row count from Sheet3
row_count = XLUtils.getRowCount(file, sheet_read)

for r in range(2, row_count + 1):
    # Read values from Sheet3
    Qty = XLUtils.readdata(file, sheet_read, r, 1)
    pp = XLUtils.readdata(file, sheet_read, r, 2)
    dis = XLUtils.readdata(file, sheet_read, r, 3)
    tax = XLUtils.readdata(file, sheet_read, r, 4)
    # Fill values into web page
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[10]//input").clear()
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[10]//input").send_keys(Qty)
    time.sleep(2)
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[11]//input").clear()
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[11]//input").send_keys(pp)
    time.sleep(2)
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[16]//input").clear()
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[16]//input").send_keys(dis)
    time.sleep(2)
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[19]//input").clear()
    driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[19]//input").send_keys(tax)
    time.sleep(2)


    # Read calculated values from webpage
    tax_value = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[20]//input").get_attribute("value")
    final_total = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[21]//input").get_attribute("value")
    gross_profit = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[22]//input").get_attribute("value")
    discount_amount = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[17]//input").get_attribute("value")
    category = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[2]//input").get_attribute("value")


    # Write to Sheet4 in xl

    XLUtils.writedata(file, sheet_write, r, 5, tax_value)
    XLUtils.writedata(file, sheet_write, r, 6, final_total)
    XLUtils.writedata(file, sheet_write, r, 7, gross_profit)
    XLUtils.writedata(file, sheet_write, r, 8, discount_amount)
    XLUtils.writedata(file, sheet_write, r, 9, category)

driver.quit()
