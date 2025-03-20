from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']") #or (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLinkQuantity']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextId"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')
SIDE_NAV_VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")

@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(15)
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message='Add to cart btn not clickable'
    ).click() ##context.driver.find_elements(*ADD_TO_CART_BTN)[2].click()

@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not visible'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ' + context.product_name)

# @when('Store product DPCI')  ##Since product name not exactly same on each page, want to verify via DPCI vs product name
# def store_product_DPCI(context):
#     context.driver.wait.until(
#         EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
#         message='Product name not visible'
#     )
#     context.product_DPCI = context.driver.find_element(By.XPATH, ("//div[@data-test='item-details-specifications']//span[contains(text(), 'DPCI')]")
# ')
#     print('Product DPCI stored: ' + context.product_DPCI)

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    #context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN), message='Add to Cart btn not clickable').click()

@when('Click on View Cart button from side navigation')
def side_nav_click_view_cart(context):
    #context.driver.find_element(*SIDE_NAV_VIEW_CART_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_VIEW_CART_BTN), message='View Cart btn not clickable').click()

