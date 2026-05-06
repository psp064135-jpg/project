from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#mac order acceptance in purchase
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
driver.find_element(By.XPATH, "//span[text()='Purchase']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Order Acceptance']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='OP No']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@id='OP No_0']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//tbody/tr[1]/td[25]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[11]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[11]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(100)
time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-check']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Dispatch Mode']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Courier Service']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@id='dispatch_details']").send_keys("online")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='validity']").send_keys(200)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='delivery']").send_keys("delivary")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='inspection']").send_keys("inspection")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='insurance']").send_keys("inspection")
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Payment Terms']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='online']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@id='delivery_remarks']").send_keys("inspection")
time.sleep(3)




