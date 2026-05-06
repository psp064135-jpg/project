from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#mac dat sales enquery
# Set file and sheet names
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
driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Sales & Marketing']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Sales Inquiry']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Inquiry Owner']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Executive-1']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Customer']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@id='Customer_0']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/div[1]/div[1]/dynamic-field-builder[1]/div[1]/div[1]/table-field[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html[1]/body[1]/p-dynamicdialog[2]/div[1]/div[1]/div[1]/sanadi-table-dialog[1]/p-table[1]/div[1]/div[2]/table[1]/thead[1]/tr[1]/th[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='p-element p-ripple p-button-success p-button-sm p-button p-component ng-star-inserted']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//tbody/tr[1]/td[10]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, " ").clear()
time.sleep(3)
driver.find_element(By.XPATH, "//p-inputnumber[@class='p-element p-inputwrapper ng-untouched ng-pristine ng-valid ng-star-inserted p-inputwrapper-filled p-inputwrapper-focus']//input[@role='spinbutton']").send_keys(100)
time.sleep(3)




