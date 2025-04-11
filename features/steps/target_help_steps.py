from behave import given, when, then
from selenium.webdriver.common.by import By

CURRENT_PROMOTIONS = (By.CSS_SELECTOR, "[class='boxSmall txtAC commonLinks']")
HELP_URL = 'https://help.target.com/help'
HELP_BTN = (By.CSS_SELECTOR, "[class='custom-h2']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@class='btn-sm search-btn']")
BROWSE_ALL_HELP = (By.CSS_SELECTOR, "[class='container clearfix'][5]")
HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
HELP_TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

@given('Open Help page')
def open_help_page(context):
    # context.driver.get('https://help.target.com/help')
    context.app.help_page.open_help_page()

@given('Open Help Returns page')
def open_help_returns_page(context):
    context.app.help_page.open_help_returns_page()

# @then('Verify Help Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
#
# @then('Verify Help Current Promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()

@when('Select Browse Help topic {dd_option_value}')
def select_browse_help_topic(context, dd_option_value):
    context.app.help_page.select_browse_help_topic(dd_option_value)

@then('Verify Help topic {dd_option_value} page opens')
def verify_help_topic_page_opens(context, dd_option_value):
    context.app.help_page.verify_help_topic_page_opens(dd_option_value)

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
    context.app.help_page.verify_all_ui_element_shown(element_amount)
    print('test case passed')





