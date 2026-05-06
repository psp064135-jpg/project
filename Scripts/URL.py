from selenium.webdriver.common.by import By
import time
#validating the URL in the application
# Launch browser and login
driver = webdriver.Chrome()
driver.get("https://uat-macdata.amigo-products.com/app/login")
driver.maximize_window()

# Login
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Sanadi@123')
driver.find_element(By.XPATH, "//span[text()='Log in']").click()
time.sleep(4)

# Navigate to Department form
driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Master']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Department']").click()
time.sleep(3)

#Validate Department form by checking URL
form_valid = False
current_url = driver.current_url

URL = "/app/masters/department"
Form = "Department"

if  URL in current_url:
    form_valid = True

# validation using visible heading
try:
    heading = driver.find_element(By.TAG_NAME, "h5").text
    if Form in heading:
        form_valid = True
except:
    pass

# Result
if form_valid:
    print(" Validation passed: You are in the Department form.")
else:
    print(f" Validation failed: Not in Department form. Current URL: {current_url}")

# Optional: Close browser
# driver.quit()
