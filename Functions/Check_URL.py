from selenium.webdriver.common.by import By
import time

def URLs(driver, URL, Form):
    form_valid = False
    current_url = driver.current_url

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
        print(" Validation passed: You are in the form:" ,Form)
    else:
        print(f" Validation failed: Not in   form. Current URL: {current_url}")


#from Functions.Check_URL import URLs
#URL = "/app/masters/designation"
#Form = "Designation"
#URLs(driver, URL, Form)
