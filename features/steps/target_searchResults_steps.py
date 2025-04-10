from behave import when, then
from time import sleep
from selenium.webdriver.common.by import By

# SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']") #or (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
# CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLinkQuantity']") # (By.CSS_SELECTOR, "[id*='addToCartButton']")
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
# SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
# SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')
# SIDE_NAV_VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="product-title"]')
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

# @when('Click on Cart icon')
# def click_cart_icon(context):
#     # context.driver.find_element(By.CSS_SELECTOR, CART_ICON)
#     context.app.searchResults_page.click_cart_icon()

# @then('Verify correct search results shown for {expected_text}')
# def verify_search_results(context, expected_text):
#     actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
#     expected_text = 'search_word'
#     assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
#     context.app.searchResults_page.verify_search_results(expected_text)
    # search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    # assert search_word in search_results_header, \
    #     f'Expected text {search_word} not in {search_results_header}'

@then('Verify {expected_text} in URL')
def verify_expected_text_url(context, expected_text):
    context.app.searchResults_page.verify_expected_text_url(expected_text)

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.searchResults_page.click_add_to_cart()
    # sleep(15)
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(ADD_TO_CART_BTN),
    #     message='Add to cart btn not clickable'
    # ).click()
    # context.driver.find_elements(*ADD_TO_CART_BTN)[2].click()

@when('Store product name')
def store_product_name(context):
    context.app.searchResults_page.store_product_name()
    # context.driver.wait.until(
    #     EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
    #     message='Product name not visible'
    # )
    # context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: '+ context.product_name)

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.searchResults_page.side_nav_click_add_to_cart()
    # context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    # sleep(5)
    # context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN), message='Add to Cart btn not clickable').click()

@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.searchResults_page.hover_fav_icon()

@then('Verify favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.searchResults_page.verify_fav_tooltip()

@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.searchResults_page.verify_search_results(expected_text)
    # actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    # expected_text == actual_text
    # assert expected_text in actual_text, f'Error. Text {expected_text} not found in {actual_text}'

@when('Click on View Cart button from side navigation')
def side_nav_click_view_cart(context):
    context.app.searchResults_page.side_nav_view_cart_btn_click()
    # context.driver.find_element(*SIDE_NAV_VIEW_CART_BTN).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_VIEW_CART_BTN), message='View Cart btn not clickable').click()

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    context.app.searchResults_page.verify_products_name_img()
    # products = context.driver.find_elements(*LISTINGS)[:8]
    #
    # for product in products:
    #     title = product.find_element(*PRODUCT_TITLE).text
    #     assert title != '', 'Product title not shown'
    #     print(title)
    #     product.find_element(*PRODUCT_IMG)

