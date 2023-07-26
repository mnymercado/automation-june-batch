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

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Coffee')
driver.find_element(By.ID, 'nav-search-submit-button').click()

sleep(3)
