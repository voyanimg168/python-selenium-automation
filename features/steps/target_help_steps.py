from behave import given, when, then
from selenium.webdriver.common.by import By

HELP_BTN = (By.CSS_SELECTOR, "[class='custom-h2']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@class='btn-sm search-btn']")
TOP_HELP_SECTION = (By.CSS_SELECTOR, "[class='container clearfix'][3]")
BOTTOM_HELP_SECTION = (By.CSS_SELECTOR, "[class='container clearfix'][4]")
BROWSE_ALL_HELP = (By.CSS_SELECTOR, "[class='container clearfix'][5]")

@given('Open target help page')
def open_help_page(context):
    # context.driver.get('https://help.target.com/help')
    context.app.help_page.open_help_page()

@when('Click on Target Help button')
def click_on_target_help_btn(context):
    # context.driver.find_element(*HELP_BTN).click()
    context.app.help_page.click_target_help_btn(HELP_BTN).click()

@when('Select Search Field')
def select_search_field(context):
    # context.driver.find_element(*SEARCH_FIELD).send_keys()  # *=multiple items
    context.app.help_page.select_search_field(SEARCH_FIELD).send_keys()

@when('Click Search button')
def click_on_search_button(context):
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.help_page.click_search_button(SEARCH_BTN).click()

@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()

@when('Select Help topic {option_value}')
def select_topic(context, option_value):
    context.app.help_page.select_topic(option_value)

# @then('Verify Help Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
#
# @then('Verify Help Current Promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()

@then('Verify Help {header} page opened')
def verify_correct_help_page_opened(context, header):
    context.app.help_page.verify_help_page_opened(header)

@when('Click on Top Help section')
def click_on_top_help(context):
    # context.driver.find_elements(*TOP_HELP_SECTION).click()
    context.app.help_page.click_on_top_help(TOP_HELP_SECTION).click()

@when('Click on Bottom Help section')
def click_on_bottom_help(context):
    # context.driver.find_elements(*BOTTOM_HELP_SECTION).click()
    context.app.help_page.click_on_bottom_help(BOTTOM_HELP_SECTION).click()

@when('Click on Browse All Help pages')
def click_on_browse_all_help(context):
    # context.driver.find_element(*BROWSE_ALL_HELP).click()
    context.app.help_page.click_browse_all_help(BROWSE_ALL_HELP).click()

@then('Verify {element_amount} UI elements on the Target Help page') ##total CSS links 2-5
def verify_all_ui_element_shown(context, element_amount):
    # element_amount = int(element_amount)
    # elements = context.driver.find_elements(By.CSS_SELECTOR, "[class='container clearfix']")
    # assert element_amount == len(elements), \
    #     f'Expected {element_amount} links, but got {len(elements)}'
    context.app.verify_all_ui_elements(element_amount)
    print('test case passed')





