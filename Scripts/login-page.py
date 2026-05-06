from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils
# screenshot with login page
driver = webdriver.Chrome()
driver.get("https://uat-macdata.amigo-products.com/app/login")
driver.maximize_window()

file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
row = XLUtils.getRowCount(file, "Sheet1")

for r in range(2, row + 1):
    username = XLUtils.readdata(file, "Sheet1", r, 1)  # Assuming username is in column 1
    password = XLUtils.readdata(file, "Sheet1", r, 2)  # Password in column 2

    # Clear input fields (important for looping)
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "password").clear()

    # Input credentials
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Click login
    driver.find_element(By.XPATH, "//span[text()='Log in']").click()

    # Wait for login processing (adjust time if needed)
    time.sleep(5)

    # Save screenshot with username
    screenshot_name = f"screenshot_{username}.png"
    driver.save_screenshot(screenshot_name)

    # Go back to login page for next attempt (adjust if your site redirects)
    driver.get("https://uat-macdata.amigo-products.com/app/login")
    time.sleep(2)

# Close browser after all iterations
driver.quit()

