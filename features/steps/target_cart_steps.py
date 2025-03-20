from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

from features.steps.target_searchResults_steps import SEARCH_RESULTS_TEXT

SEARCH_RESULTS_MESSAGE = (By.CSS_SELECTOR, "[@data-test='boxEmptyMsg']")
CART_ICON = (By.XPATH, "//div[@data-test='@web/CartIcon']")
CART_SUMMARY = (By.CSS_SELECTOR, '[class*="h-margin-b-tight"] span') #or (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@when('Open cart page')
def open_cart_page(context):
    context.browser.find_element(*CART_ICON).click() #or context.driver.get('https://www.target.com/cart')

@then('Verify cart has correct product')
def verify_product_name(context):
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print('Name in cart: ' + product_name_in_cart)
    assert context.product_name[:40] == product_name_in_cart[:40], \
        f'Expected {context.product_name[:40]} did not match {product_name_in_cart[:40]}'

@then('Verify cart has {amount} items')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f'Expected {amount} items not in {cart_summary}'

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Expected {expected_text} did not match {actual_text}'

