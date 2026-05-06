
#import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

#web driver
#leave entry
driver = webdriver.Chrome()
driver.get("https://uat-skdsirihrm.amigo-products.com/app/login")
driver.maximize_window() #login page
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('admin@sanadi.com')
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('Sanadi@123') #enter key
driver.find_element(By.XPATH,"//span[text()='Sign In']").click()
time.sleep(3)#click on text
driver.find_element(By.XPATH,"//span[@class='p-button-icon pi pi-bars']").click()
time.sleep(3) #click on menu
driver.find_element(By.XPATH,"//span[text()='Master']").click()
time.sleep(3) #click on button
driver.find_element(By.XPATH," //span[normalize-space()='Leave Entry']").click()
time.sleep(3)#grade name
driver.find_element(By.CSS_SELECTOR, ".p-element.primary.p-button.p-component.ng-star-inserted").click()
#new button
#driver.find_element(By.XPATH,"").send_keys('')
time.sleep(3)
#for sick leave with full and half leave

driver.find_element(By.XPATH,"//div[@id='Employee Code']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)#emp name
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Employee-50 | yash | Tester']").click()
time.sleep(3)#emp name from dropdown field
driver.find_element(By.XPATH,"//div[@id='Leave Type']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Sick Leave']").click()
time.sleep(3)#options
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/sanadi-accordion[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/div[5]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(5)# xpath of calender,
driver.find_element(By.XPATH,"//span[normalize-space()='21']").click()
time.sleep(3) # from date
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/sanadi-accordion[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/div[6]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]/calendaricon[1]/*[name()='svg'][1]").click()
time.sleep(5)# xpath of calender,
driver.find_element(By.XPATH,"//span[normalize-space()='22']").click()
time.sleep(3) # to date
driver.find_element(By.XPATH,"//div[@id='Condition']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#condition
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Full Day']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//textarea[@id='reason']").send_keys('due to high feaver and headace')
time.sleep(3)#reason
driver.find_element(By.XPATH,"//textarea[@id='remarks']").send_keys('cannot attend the office for 2 days')
time.sleep(5) #remarks
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(5)  # save button

#save-edit-save for casuaul leave and LOP
driver.find_element(By.CSS_SELECTOR, ".p-element.primary.p-button.p-component.ng-star-inserted").click()
time.sleep(3)#new button
driver.find_element(By.XPATH,"//div[@id='Employee Code']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)#emp name
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Employee-51 | yashwanthaf | Tester']").click()
time.sleep(3)#emp name from dropdown field

driver.find_element(By.XPATH,"//div[@id='Leave Type']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Casual Leave']").click()
time.sleep(3)#options
driver.find_element(By.CSS_SELECTOR,"p-inputswitch[class='p-element ng-untouched ng-pristine ng-valid'] span[class='p-inputswitch-slider']").click()
time.sleep(3)#LOP
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/sanadi-accordion[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/div[5]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(5)# xpath of calender,
driver.find_element(By.XPATH,"//span[normalize-space()='22']").click()
time.sleep(3) # from date
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/sanadi-accordion[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/div[6]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]/calendaricon[1]/*[name()='svg'][1]").click()
time.sleep(5)# xpath of calender,
driver.find_element(By.XPATH,"//span[normalize-space()='25']").click()
time.sleep(3) # to date
driver.find_element(By.XPATH,"//div[@id='Condition']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Half Day']").click()
time.sleep(3)#option
driver.find_element(By.XPATH,"//textarea[@id='reason']").send_keys('due to family trip')
time.sleep(3)#reason
driver.find_element(By.XPATH,"//textarea[@id='remarks']").send_keys('cannot attend the office for 4 days')
time.sleep(5)#remarks
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(10)#save button


#save-edit-save for earned leave and comp off
driver.find_element(By.CSS_SELECTOR, ".p-element.primary.p-button.p-component.ng-star-inserted").click()
time.sleep(3)#new button
driver.find_element(By.XPATH,"//div[@id='Employee Code']//div[@aria-label='dropdown trigger']").click()
time.sleep(3)#emp name
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Employee-52 | meshueee | Tester']").click()
time.sleep(3)#emp name from dropdown field

driver.find_element(By.XPATH,"//div[@id='Leave Type']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Earned Leave']").click()
time.sleep(3)#options
driver.find_element(By.CSS_SELECTOR,"body > p-dynamicdialog:nth-child(85) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > sanadi-dialog:nth-child(1) > dynamic-form-builder:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > tab:nth-child(2) > p-tabview:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p-tabpanel:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(7) > dynamic-field-builder:nth-child(1) > div:nth-child(1) > div:nth-child(2) > sanadi-accordion:nth-child(1) > p-accordion:nth-child(1) > div:nth-child(1) > p-accordiontab:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > dynamic-field-builder:nth-child(1) > div:nth-child(1) > div:nth-child(2) > slide-toggle:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p-inputswitch:nth-child(1) > div:nth-child(1) > span:nth-child(2)").click()
time.sleep(3)#comp off
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/sanadi-accordion[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/div[5]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(5)#xpath of calender,
driver.find_element(By.XPATH,"//span[normalize-space()='22']").click()
time.sleep(3)#from date
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/sanadi-accordion[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/div[6]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]/calendaricon[1]/*[name()='svg'][1]").click()
time.sleep(5)#xpath of calender,
driver.find_element(By.XPATH,"//span[normalize-space()='22']").click()
time.sleep(3)#to date
driver.find_element(By.XPATH,"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/sanadi-dialog[1]/dynamic-form-builder[1]/form[1]/div[1]/div[1]/tab[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[1]/div[1]/div[1]/div[7]/dynamic-field-builder[1]/div[1]/div[1]/sanadi-accordion[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/div[9]/dynamic-field-builder[1]/div[1]/div[1]/date[1]/div[1]/div[1]/p-calendar[1]/span[1]/button[1]").click()
time.sleep(5)#xpath of calender comp off,
driver.find_element(By.XPATH,"//span[normalize-space()='23']").click()
time.sleep(3)#comp off date

driver.find_element(By.XPATH,"//div[@id='Condition']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown field
driver.find_element(By.XPATH,"//div[@class='p-element elipsis'][normalize-space()='Full Day']").click()
time.sleep(3)#option
driver.find_element(By.XPATH,"//textarea[@id='reason']").send_keys('due to balence earned leave')
time.sleep(3)#reason
driver.find_element(By.XPATH,"//textarea[@id='remarks']").send_keys('cannot attend the office for 3 days')
time.sleep(5) #remarks
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(10)  # save button

#once again check the below code
driver.find_element(By.XPATH,"//tbody/tr[1]/td[8]/div[1]/button[1]").click()
time.sleep(3)#edit button
driver.find_element(By.XPATH,"//div[@id='pn_id_117']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown button
driver.find_element(By.XPATH,"//li[@id='pn_id_117_0']").click()
time.sleep(6)#edit button
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(6)#save button

#to reject
driver.find_element(By.XPATH,"//tbody/tr[2]/td[8]/div[1]/button[1]/span[1]").click()
time.sleep(3)#edit button
driver.find_element(By.XPATH,"//div[@id='pn_id_117']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown button
driver.find_element(By.XPATH,"//span[text()='Rejected']").click()
time.sleep(6)#edit button
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(6)#save button

# to cancel
driver.find_element(By.XPATH,"//tbody/tr[3]/td[8]/div[1]/button[1]").click()
time.sleep(3)#edit button
driver.find_element(By.XPATH,"//div[@id='pn_id_117']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']").click()
time.sleep(3)#dropdown button
driver.find_element(By.XPATH,"//span[text()='Cancelled']").click()
time.sleep(6)#edit button
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
time.sleep(600)#save button



