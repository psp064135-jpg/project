#employee details
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# grade master, employee
# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window() #login page
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('Sanadi@123') #enter key
driver.find_element(By.XPATH,"//span[text()='Sign In']").click() #click on text
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='p-button-icon pi pi-bars']").click()
time.sleep(3) #click on menu
driver.find_element(By.XPATH,"//span[text()='Master']").click()
time.sleep(3) #click on button
driver.find_element(By.XPATH," //span[normalize-space()='Employee']").click()
time.sleep(3)#grade name
driver.find_element(By.CSS_SELECTOR,".p-element.primary.p-button.p-component.ng-star-inserted").click()
time.sleep(3) #new button
driver.find_element(By.XPATH,"//input[@name='employee_card_number']").send_keys('EMP2')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='biometric_key']").send_keys('EMPLOYE')
time.sleep(3)
driver.find_element(By.XPATH,"//span[@aria-label='Select Title']").click()
time.sleep(5) #dropdown field
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Mr']"))).click()
driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys('meshu')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='last_name']").send_keys('s')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='father_or_husband_name']").send_keys('kumar')
time.sleep(3)#husband name

driver.find_element(By.XPATH,"//div[@id='Employee Type']//div[@aria-label='dropdown trigger']").click()
time.sleep(3) #dropdown field of type
driver.find_element(By.XPATH, "//div[@class='p-element elipsis'][normalize-space()='Test']").click()
time.sleep(3) #select option

driver.find_element(By.XPATH,"//span[@aria-label='Select Department']").click()
time.sleep(3) #dropdown field
driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys('dep')
time.sleep(3) #click on button
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Department 1']").click()
time.sleep(3) #click on button

driver.find_element(By.XPATH,"//div[@id='Designation']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3) #dropdown field of designation
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Tester']").click()
time.sleep(3) #select option

driver.find_element(By.XPATH,"//div[@id='Grade Master']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(5) #grade master
driver.find_element(By.XPATH,"//li[@id='Grade Master_2']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='device_id']").send_keys("ASUS1")
time.sleep(3) #device id
driver.find_element(By.XPATH,"//div[@id='First Reporting Authority']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(5) #first reporting authority
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Employee-49 | Ganga | Tester']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@id='Second Report Authority']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(5) # second reporting authority
driver.find_element(By.XPATH,"//li[@id='Second Report Authority_1']//div[@class='item-item ng-star-inserted']").click()
time.sleep(3)
#basic details
driver.find_element(By.XPATH,"//span[text()='Basic Details']").click()
time.sleep(3) #basic details
driver.find_element(By.XPATH, "//button[@aria-label='Choose Date']").click()
time.sleep(5)#attribute of calender, date of birth
driver.find_element(By.XPATH, " //button[@aria-label='Choose Year']").click()
time.sleep(3)#selecting 2025 xpath
driver.find_element(By.XPATH, "//span[normalize-space()='2021']").click()
time.sleep(3)#selecting year
driver.find_element(By.XPATH,"//span[normalize-space()='May']").click()
time.sleep(3) #click on may month
driver.find_element(By.XPATH,"//span[normalize-space()='10']").click()
time.sleep(3) #date

driver.find_element(By.XPATH,"//button[@aria-label='Choose Date']").click()
time.sleep(5)#attribute of calender, date of birth
driver.find_element(By.XPATH,"//button[@aria-label='Choose Year']").click()
time.sleep(3)#selecting 2025 xpath
driver.find_element(By.XPATH,"//span[normalize-space()='2021']").click()
time.sleep(3)#selecting year
driver.find_element(By.XPATH,"//span[normalize-space()='May']").click()
time.sleep(3) #click on may month
driver.find_element(By.XPATH,"//span[normalize-space()='10']").click()
time.sleep(3) #date

driver.find_element(By.XPATH,"//calendaricon[@class='p-element p-icon-wrapper ng-tns-c1784716240-59 ng-star-inserted']//*[name()='svg']").click()
time.sleep(5)#attribute of calender,date of joining
driver.find_element(By.XPATH,"//button[@aria-label='Choose Year']").click()
time.sleep(3)#selecting 2025 xpath
driver.find_element(By.XPATH,"//span[normalize-space()='2022']").click()
time.sleep(3)#selecting year
driver.find_element(By.XPATH,"//span[normalize-space()='May']").click()
time.sleep(3) #click on may month
driver.find_element(By.XPATH,"//span[normalize-space()='10']").click()
time.sleep(3) #date

driver.find_element(By.XPATH,"//button[@class='p-element p-ripple p-datepicker-trigger p-button-icon-only ng-tns-c1784716240-60 p-button p-component ng-star-inserted']").click()
time.sleep(5)#attribute of calender,
driver.find_element(By.XPATH,"//button[@aria-label='Choose Year']").click()
time.sleep(3)#selecting 2025 xpath
driver.find_element(By.XPATH,"//span[normalize-space()='2024']").click()
time.sleep(3)#selecting year
driver.find_element(By.XPATH,"//span[normalize-space()='Jan']").click()
time.sleep(3) #click on may month
driver.find_element(By.XPATH,"//span[normalize-space()='15']").click()
time.sleep(3) #date

driver.find_element(By.XPATH,"//button[@class='p-element p-ripple p-datepicker-trigger p-button-icon-only ng-tns-c1784716240-61 p-button p-component ng-star-inserted']").click()
time.sleep(5)#attribute of calender,
driver.find_element(By.XPATH,"//button[@aria-label='Choose Year']").click()
time.sleep(3)#selecting 2025 xpath
driver.find_element(By.XPATH,"//span[normalize-space()='2023']").click()
time.sleep(3)#selecting year
driver.find_element(By.XPATH,"//span[normalize-space()='Dec']").click()
time.sleep(3) #click on may month
driver.find_element(By.XPATH,"//span[normalize-space()='6']").click()
time.sleep(3) #date

driver.find_element(By.XPATH,"//input[@id='mobile_number']").send_keys('7760498719')
time.sleep(3) #phone no.
driver.find_element(By.XPATH,"//input[@id='alternate_mobile_number']").send_keys('7760489712')
time.sleep(3) #alternate phone no.
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('lsyashwanth1@gmail.com')
time.sleep(3) #mailid
driver.find_element(By.XPATH,"//div[@id='Marital Status']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#martial status
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Unmarried']").click()
time.sleep(3)#select option
driver.find_element(By.CSS_SELECTOR,"div[id='Gender'] div[aria-label='dropdown trigger']").click()
time.sleep(3)#gender
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Male']").click()
time.sleep(3)#male
driver.find_element(By.CSS_SELECTOR,"div[id='Blood Group'] div[aria-label='dropdown trigger']").click()
time.sleep(3)#blood group
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='A+']").click()
time.sleep(3)#select option
driver.find_element(By.CSS_SELECTOR,"div[id='Religion Type'] chevrondownicon[class='p-element p-icon-wrapper ng-star-inserted'] svg").click()
time.sleep(3)#relegion type
driver.find_element(By.XPATH,"//li[@id='Religion Type_0']").click()
time.sleep(3)#select option
driver.find_element(By.CSS_SELECTOR,"div[id='Health Issue'] chevrondownicon[class='p-element p-icon-wrapper ng-star-inserted'] svg").click()
time.sleep(3)#health issue
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='No']").click()
time.sleep(3)#select option
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys('vinoba nagara, shivamoga, karnataka')
time.sleep(3) #addres
driver.find_element(By.XPATH,"//input[@id='postal_code']").send_keys('577212')
time.sleep(3) #postal code
driver.find_element(By.XPATH,"//input[@id='pf_account_number']").send_keys('TN/MAS/1234567/000001')
time.sleep(3) #pf account number
driver.find_element(By.XPATH,"//input[@id='uan_number']").send_keys('100200300400')
time.sleep(3) #UAN number
driver.find_element(By.XPATH,"//input[@id='esi_number']").send_keys('12345678901234567')
time.sleep(3) #ESI number
driver.find_element(By.XPATH,"//input[@id='aadhar_number']").send_keys('1234 5678 9123')
time.sleep(3) #Aadhar no.
driver.find_element(By.XPATH,"//input[@id='pan_card']").send_keys('ABCDE1234F')
time.sleep(3) #PAN card number

#next
driver.find_element(By.XPATH,"//button[@label='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//p-table//thead/tr[1]/th[8]//button/span").click()
time.sleep(3) #add button by attribute
driver.find_element(By.XPATH,"//button[@icon='pi pi-pencil']").click()
time.sleep(4) #edit button use attribute
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[2]/p-celleditor[1]/input[1]").send_keys('sanadi tec.')
time.sleep(3) #company name
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[3]/p-celleditor[1]/input[1]").send_keys('123123123')
time.sleep(3) #PF account number
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[4]/p-celleditor[1]/input[1]").send_keys('123123')
time.sleep(3) #UAN number
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[5]/p-celleditor[1]/input[1]").send_keys('789789789')
time.sleep(3) #PR number
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[6]/p-celleditor[1]/input[1]").send_keys('456456456')
time.sleep(3) #Insurence number
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[7]/p-celleditor[1]/input[1]").send_keys('675675675')
time.sleep(3) #ESI number
driver.find_element(By.XPATH,"//button[@icon='pi pi-check']").click()
time.sleep(3) #save button use attribute
#next

driver.find_element(By.XPATH,"//button[@label='Next']").click()
time.sleep(3)#next
driver.find_element(By.XPATH,"//input[@id='bank_name']").send_keys('canara bank')
time.sleep(3) #bank name
driver.find_element(By.XPATH,"//input[@id='account_number']").send_keys('123123123')
time.sleep(3) #account number
driver.find_element(By.XPATH,"//input[@id='ifsc_code']").send_keys('ABC123')
time.sleep(3) #IFSE code
driver.find_element(By.XPATH,"//input[@id='beneficiary_code']").send_keys('San@123')
time.sleep(3) #beneficary code
driver.find_element(By.XPATH,"//div[@id='Nominee Relationship']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Father']").click()
time.sleep(3) #nominee name
driver.find_element(By.XPATH,"//input[@id='nominee_name']").send_keys('yashu')
time.sleep(3) #nominee name
driver.find_element(By.XPATH,"//input[@id='nominee_aadhar_number']").send_keys('321321321')
time.sleep(3) #nominee aadhar no.
driver.find_element(By.XPATH,"//input[@id='nominee_mobile_number']").send_keys('7760498798')
time.sleep(300) #nominee mob no

#sleep for 300 seconds

driver.find_element(By.XPATH,"//p-table//thead[1]/tr[1]/th[4]//button[1]/span[1]").click()
time.sleep(3) #add button by attribute
driver.find_element(By.XPATH,"//button[@icon='pi pi-pencil']").click()
time.sleep(4) #edit button use attribute
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[2]/p-celleditor[1]/input[1]").send_keys('HLT234')
time.sleep(3) #policy number
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[3]/p-celleditor[1]/input[1]").send_keys('5000000')
time.sleep(3) #amount
driver.find_element(By.XPATH,"//button[@icon='pi pi-check']").click()
time.sleep(3) # save button
driver.find_element(By.XPATH,"//button[@icon='pi pi-upload']").click()
time.sleep()  #export

time.sleep(3)
driver.quit()