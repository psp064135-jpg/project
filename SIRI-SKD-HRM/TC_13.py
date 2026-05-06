from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#salary incorrect calculation
# Launch the chrome and open the website
driver = webdriver.Chrome()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window()

# Login
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Sanadi@123')
driver.find_element(By.XPATH, "//span[text()='Sign In']").click()

time.sleep(3)

# Navigate to Salary Calculation
driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-bars']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='HRM']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Salary Calculation']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".p-element.primary.p-button.p-component.ng-star-inserted").click()  # New button

# Select From and To dates
driver.find_element(By.XPATH, "//p-tabpanel[1]/div[1]/div[1]/div[1]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='1']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//p-tabpanel[1]/div[1]/div[1]/div[2]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[4]/span[1]").click()

# Select Test option from dropdown
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-multiselect-trigger']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-element'][normalize-space()='Test']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-multiselect-trigger']").click()

# Click the Edit button
time.sleep(2)
driver.find_element(By.XPATH, "//tbody[1]/tr[2]/td[16]/div[1]/button[1]").click()
#edit button
time.sleep(5)
#values from input fields
num1 = driver.find_element(By.XPATH, "//tbody[1]/tr[2]/td[8]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]")
time.sleep(5)
num2 = driver.find_element(By.XPATH, "//tbody[1]/tr[2]/td[9]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]")
#converting the values to integer
value1 = int(num1.get_attribute("aria-valuenow"))
value2 = int(num2.get_attribute("aria-valuenow"))
# Expected sum
expected_sum = value1 + value2
time.sleep(5)
# Get actual result value
result_element = driver.find_element(By.XPATH, "//tbody[1]/tr[2]/td[15]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]")
actual_sum = int(result_element.get_attribute("aria-valuenow"))
# Compare the values
if expected_sum == actual_sum:
    print("The sum is correct")
else:
    print("The sum is incorrect")
    #print(f"Expected: {expected_sum}, but got: {actual_sum}")
# Close browser
driver.quit()
