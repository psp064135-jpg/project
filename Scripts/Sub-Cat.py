#Sub Category Master by taking the data from xl even for search field also,
#taking the category master data from xl
#creating the reuseable for the login credientials
import sys
import os
# Add the 'Functions' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Functions')))
from login import login  # Now this will work
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functions import XLUtils
driver = login()  # This launches browser and logs in

driver.find_element(By.XPATH, "//span[text()='Master']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Sub Category Master']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='+ Add New']").click()
time.sleep(3)

file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
sheet_cat = "Category"
row_count = XLUtils.getRowCount(file, sheet_cat)
for r in range(2, row_count + 1):
    category_name = XLUtils.readData(file, sheet_cat, r, 1)
    driver.find_element(By.XPATH, "//button[@class='p-element primary custom-dropdwon-button p-button p-component p-button-icon-only ng-star-inserted']").click()
    time.sleep(2)
    driver.find_element(By.ID, "category_name").send_keys(category_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//html[1]/body[1]/p-dynamicdialog[2]/div[1]/div[1]/div[3]/sanadi-dialog-footer[1]/div[1]/div[2]/button[2]").click()
    time.sleep(3)
    # Delete the row from the Excel file after processing
    XLUtils.deleteRow(file,sheet_cat, 2) # Delete the first row (index 2)
    # Stop after processing the first row (if needed for just one iteration)
# File and sheet path
    file = "C:\\Users\\Asus\\OneDrive\\Documents\\login.xlsx"
    sheet = "Sub_category"
# Loop through the data and process it
    while XLUtils.getRowCount(file, sheet) >= 2:  # Make sure there are rows to process
        sub_category_name = XLUtils.readData(file, sheet, 2, 1)  # Read category name from column 1
        search = XLUtils.readData(file, sheet, 2, 2)

        driver.find_element(By.XPATH, "//div[@id='Category']//div[@aria-label='dropdown trigger']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(search)
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Cat-30']").click()
        time.sleep(3)
        driver.find_element(By.ID, "sub_category_name").send_keys(sub_category_name)
        time.sleep(2)# Save the new category
        driver.find_element(By.XPATH, "/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[3]/sanadi-dialog-footer[1]/div[1]/div[3]/button[2]").click()
        time.sleep(3)
    # Delete the row from the Excel file after processing
        XLUtils.deleteRow(file,sheet, 2)  # Delete the first row (index 2)
    # Stop after processing the first row (if needed for just one iteration)
    #close the loop
        driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[3]/div[1]/button[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@aria-label='Yes']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@label='Inactive']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Search keyword']").send_keys("subcat-4")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='p-element p-button-outlined secondary md:hidden lg:flex xl:flex p-button p-component']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@label='Active']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Search keyword']").send_keys("tons4")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@aria-label='Show Filter Menu']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@class='p-inputtext p-component p-element ng-star-inserted']").send_keys("cat-33")
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Apply']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='p-element p-button-outlined secondary md:hidden lg:flex xl:flex p-button p-component']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@icon='pi pi-upload']").click()
        time.sleep(300)
time.sleep(300)