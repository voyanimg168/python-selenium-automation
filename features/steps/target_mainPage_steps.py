from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_FIELD = (By.ID, 'search_word')
# SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
# CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']") #or [data-test='@web/CartLink']
# SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")  #or (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
# HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")

@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()
    # context.driver.get('https://www.target.com/')
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SEARCH_FIELD),
    #     message='Search field not clickable'
    # ) #EC every 500 ms vs IW every 100 ms

@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search_product(search_word)
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)  # *=multiple items
    # context.driver.find_element(*SEARCH_BTN).click()
    # ------
    # context.driver.find_element(By.ID, 'search').send_keys(search_word)
    # context.driver.find_element(By.CSS_SELECTOR, "[@data-test='@web/Search/SearchButton']").click()

@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()
    # context.driver.find_element(*CART_ICON).click()
    # context.driver.wait.until(
    #   EC.element_to_be_clickable(CART_ICON),
    #   message='Cart btn not clickable'
    #   )

@then('Verify at least 1 link shown')
def verify_1_header_link(context):
    context.app.header.verify_1_header_link()
#     link = context.driver.find_element(*HEADER_LINKS)
#     print(link)
#
    # link = context.driver.find_element(*HEADER_LINKS)
    # print('Before refresh: ', link)
    # context.driver.refresh()
    # link = context.driver.find_element(*HEADER_LINKS)
    # print('After refresh: ', link)
#
    # Stale Element Reference Example
    # print('Before refresh: ', link)
    # context.driver.refresh()
    # link = context.driver.find_element(*HEADER_LINKS)
    # link.click()
    # print('After refresh: ', link)

@then('Verify {link_amount} header links are shown') ##total 6 links
def verify_all_header_links_shown(context, link_amount):
    context.app.header.verify_all_header_links_shown(link_amount)
    # links = context.driver.find_elements(*HEADER_LINKS)
    # assert len(links) == 6, f'Expected 6 links, but got {len(links)}'
    # print(links)
    # Error with this because string != integer so modify below
    # -------------------------
    # link_amount = int(link_amount)
    # links = context.driver.find_elements(*HEADER_LINKS)
    # print(links)
    # assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'





