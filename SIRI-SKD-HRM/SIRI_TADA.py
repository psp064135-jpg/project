from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# for calcuating the TA/DA form
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
driver.find_element(By.XPATH,"//span[@class='p-button-icon pi pi-bars']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[text()='HRM']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='TA/DA Form']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".p-element.primary.p-button.p-component.ng-star-inserted").click()  # New button
time.sleep(3)
#dropdown field
driver.find_element(By.XPATH,"//div[@id='Employee']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='yashu | Employee-56']").click()
time.sleep(3)#option

#travel expence
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[6]/div[1]/button[2]").click()
time.sleep(3)#edit button
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys("3000")
time.sleep(3)#enter amount
num1 = driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]")
num5 = driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/number[1]/div[1]/div[1]/p-inputnumber[1]/span[1]/input[1]")
#converting the values to integer
value1 = int(num1.get_attribute("aria-valuenow"))
value5 = int(num5.get_attribute("aria-valuenow"))
if  value1 ==  value5 :
    print("travel expenses is correct")
else:
    print("travel expenses is incorrect")
    driver.quit

#food expence
driver.find_element(By.XPATH,"//tbody[1]/tr[2]/td[6]/div[1]/button[2]/span[1]").click()
time.sleep(3)#food expence edit button
driver.find_element(By.XPATH,"//tbody[1]/tr[2]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(4000)
time.sleep(3)#enter amount
num2 = driver.find_element(By.XPATH,"//tbody[1]/tr[2]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]")
num5 = driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/number[1]/div[1]/div[1]/p-inputnumber[1]/span[1]/input[1]")
#converting the values to integer
value2 = int(num2.get_attribute("aria-valuenow"))
value5 = int(num5.get_attribute("aria-valuenow"))
value_2 = value1 + value2
time.sleep(3)
if  value_2 == value5 :
    print("Food expenses is correct")
else:
    print("Food expenses is incorrect")
    driver.quit

# Hotel expence
driver.find_element(By.XPATH,"//tbody[1]/tr[3]/td[6]/div[1]/button[2]").click()
time.sleep(3)#food expence edit button
driver.find_element(By.XPATH,"//tbody[1]/tr[3]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(5000)
time.sleep(3)#enter amount
num3 = driver.find_element(By.XPATH,"//tbody[1]/tr[3]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]")
num5 = driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/number[1]/div[1]/div[1]/p-inputnumber[1]/span[1]/input[1]")
#converting the values to integer
value3 = int(num3.get_attribute("aria-valuenow"))
value5 = int(num5.get_attribute("aria-valuenow"))
value_3 = value1 + value2 + value3
time.sleep(3)
if  value_3 == value5 :
    print("Hotel expenses is correct")
else:
    print("Hotel expenses is incorrect")
    driver.quit

# Other expence
driver.find_element(By.XPATH,"//tbody[1]/tr[4]/td[6]/div[1]/button[2]").click()
time.sleep(3)#food expence edit button
driver.find_element(By.XPATH,"//tbody[1]/tr[4]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]").send_keys(2000)
time.sleep(3)#enter amount
num4 = driver.find_element(By.XPATH,"//tbody[1]/tr[4]/td[5]/p-celleditor[1]/p-inputnumber[1]/span[1]/input[1]")
num5 = driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/number[1]/div[1]/div[1]/p-inputnumber[1]/span[1]/input[1]")
#converting the values to integer
value4 = int(num4.get_attribute("aria-valuenow"))
value5 = int(num5.get_attribute("aria-valuenow"))
value_4 = value1 + value2 + value3 + value4
time.sleep(3)
if  value_4 == value5 :
    print("Other expenses is correct")
else:
    print("Other expenses is incorrect")
    driver.quit


driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[6]/div[1]/button[2]").click()
time.sleep(3)#save buttons
driver.find_element(By.XPATH,"//tbody[1]/tr[2]/td[6]/div[1]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//tbody[1]/tr[3]/td[6]/div[1]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//tbody[1]/tr[4]/td[6]/div[1]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='p-dialog-footer ng-tns-c3034771475-159 ng-star-inserted']//button[2]").click()
time.sleep(3)
driver.quit()