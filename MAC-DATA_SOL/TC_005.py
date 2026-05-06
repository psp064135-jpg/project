from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils

#mac dat sales quotation
# Set file and sheet names
file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet_read = "Sheet3"

# Launch browser and login
driver = webdriver.Chrome()
driver.get("https://uat-macdata.amigo-products.com/app/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Sanadi@123')
driver.find_element(By.XPATH, "//span[text()='Log in']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Sales & Marketing']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Sales Quotation']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Quotation Type']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@id='Quotation Type_1']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//p-calendar[1]/span[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='12']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//p-calendar[1]/span[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='16']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Assign To']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='admin |']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Customer']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Customer-3']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/div[1]/div[2]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/div[1]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-checkbox-box']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='p-element p-ripple p-button-success p-button-sm p-button p-component ng-star-inserted']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//tbody/tr[1]/td[21]/div[1]/button[1]").click()
time.sleep(3)

file="C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
row = XLUtils.getRowCount(file, "Sheet5")
for r in range(2, row + 1):
     qty = XLUtils.readdata(file, "Sheet5", r, 2)
     pp = XLUtils.readdata(file, "Sheet5", r, 2)
     up = XLUtils.readdata(file, "Sheet5", r, 2)
     dis = XLUtils.readdata(file, "Sheet5", r, 2)

driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[8]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(qty)
time.sleep(3)#qty
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[9]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(pp)
time.sleep(3)#purchase price
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[10]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(up)
time.sleep(3)#unite price
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[14]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(dis)
time.sleep(3)#discount

