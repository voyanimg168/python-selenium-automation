from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# @given('Open target main page')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')
#
# @when('Search for {search_word}') #3928 results for sofa
# def search_product(context, search_word):
#     context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)  # *=multiple items
#     context.driver.find_element(*SEARCH_BTN).click()
#     sleep(2) #use this vs EC if element is ephemeral; only use EC for long-term items

@then('Verify every product on {search_word} search results page has name and image')
def verify_product_name_and_image(context, search_word):
    search_results = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="product-grid"] [data-test="@web/site-top-of-funnel/ProductCardWrapper"]')
    image_locator = context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/ProductCard/ProductCardImage"]')
    product_title = context.driver.find_element(By.CSS_SELECTOR, '[data-test="product-title"]')

    for product in search_results:
        assert image_locator is not None, f'No image found'
        assert product_title is not None, f'No product title found'


