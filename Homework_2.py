from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path='/Users/nicolemercado/automation-june-batch/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# OPEN AMAZON
driver.get('https://www.amazon.com/')

sleep(8)
#CLICK ORDERS
driver.find_element(By.ID, 'nav-orders').click()

#VERIFY SIGN IN PAGE IS OPEN
#Sign in Header is Visible
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class = 'a-spacing-small']").text
assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
assert driver.find_element(By.ID, 'ap_email'), f'Email input field not present' #email input field


driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']") #Amazon Logo
driver.find_element(By.ID, 'ap_email') #email input field
driver.find_element(By.ID, 'continue') #Continue BTN
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]") #Conditions of Use Link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']") #Other solution Conditions of Use Link using text(), this will only work on XPATH
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]") #Privacy Notice Link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click() #Need help Link
driver.find_element(By.ID, 'auth-fpp-link-bottom') #Forgot Password BTN
driver.find_element(By.ID, 'ap-other-signin-issues-link') #Other issues with Sign-In Link
driver.find_element(By.ID, 'createAccountSubmit') #Create your Amazon Account BTN
