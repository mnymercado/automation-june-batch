from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path='/Users/nicolemercado/automation-june-batch/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#BY XPATH
#Tag and attribute
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_customerservice']")

#Multiple Attributes
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_customerservice' and @data-csa-c-slot-id='nav_cs_1']")

#By XPATH, text
driver.find_element(By.XPATH, "//a[text()='Customer Service' and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[text()='Gift Cards']")

#Any tag = *
driver.find_element(By.XPATH, "//*[text()='Customer Service' and @class='nav-a  ']")

#Contains
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_customerservice')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'er Service') and @class='nav-a  ']")


print('Test Passed')

driver.quit()