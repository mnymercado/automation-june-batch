from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@when('Click result')
def click_result(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-cel-widget="MAIN-SEARCH_RESULTS-2"] span.a-price-whole').click()


@when('Click add to cart btn')
def click_add_to_cart_btn(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@when('Click go to cart btn')
def click_goto_cart_btn(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span#sw-gtc .a-button-inner').click()


@then('Verify cart not empty')
def verify_cart_not_empty(context):
    actual_result = context.driver.find_element(By.ID, 'sc-subtotal-label-buybox').text
    print(actual_result)
    expected_result = '1'
    assert expected_result in actual_result, f'{expected_result} not in {actual_result}'
