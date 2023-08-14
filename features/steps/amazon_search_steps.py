from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(8)


@when('Search for table')
def search_text(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify search result is correct')
def verify_result(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1.s-desktop-toolbar span.a-text-bold").text
    expected_result = '"table"'
    assert actual_result in expected_result, f'Expected {expected_result} not in {actual_result}'


@when('Click Orders')
def click_orders_btn(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify sign in page opened')
def verify_signin_page_opened(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    expected_result = 'Sign in'
    assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'
    context.driver.find_element(By.ID, 'ap_email')


@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').text
    expected_result = 'Your Amazon Cart is empty'
    assert actual_result == expected_result, f'Expected result is {expected_result} but got {actual_result}'
