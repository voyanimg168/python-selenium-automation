from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")  #or (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)  # *=multiple items
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(2) #use this vs EC if element is ephemeral; only use EC for long-term items

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON), message='Cart btn not clickable').click()

@then('Verify at least 1 link shown')
def verify_1_header_link(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)

@then('Verify {link_amount} header links are shown') ##total 6 links
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'




