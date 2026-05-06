# Trial_1.py

import time
from selenium.webdriver.common.by import By
from Functions.login1 import login1  # Login function returning a WebDriver

Module = 'Master'
SubModule = 'Product Master'

driver = login1(Module, SubModule)
time.sleep(2)

# You can uncomment this when needed
# from Functions.Delete_export import delete_and_export
# delete_and_export(driver)

# URL = "/app/masters/Product"
# Form = "Designation"
# from Functions.Check_URL import URLs
# URLs(driver, URL, Form)



