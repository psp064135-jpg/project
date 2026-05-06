from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#mac Purchase order in purchase
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
driver.find_element(By.XPATH, "//span[normalize-space()='Purchase Order']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Supplier Name']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='C&S']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='OA Number']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='OA 0018 | Customer-3']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Delivery Terms']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='full payment']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Delivery Method']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='online']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Delivery Method']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='online']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//p-calendar[1]/span[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='14']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='Contact Person']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Emp-21 | Varun | Sales']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@id='remarks']").send_keys("inspection")
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@id='bank_address']").send_keys("inspection")
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[17]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[8]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys("10")
time.sleep(3)
driver.find_element(By.XPATH, "//tbody[1]/tr[1]/td[17]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Add Terms']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='p-checkbox-box']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='p-element p-ripple p-button-success p-button-sm p-button p-component ng-star-inserted']").click()
time.sleep(30)





