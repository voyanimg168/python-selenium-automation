from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

HELP_BTN = (By.CSS_SELECTOR, "[class='custom-h2']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@class='btn-sm search-btn']")
TOP_HELP_SECTION = (By.CSS_SELECTOR, "[class='container clearfix'][3]")
BOTTOM_HELP_SECTION = (By.CSS_SELECTOR, "[class='container clearfix'][4]")
BROWSE_ALL_HELP = (By.CSS_SELECTOR, "[class='container clearfix'][5]")

@given('Open target help page')
def open_help_page(context):
    context.driver.get('https://help.target.com/help')

@when('Click on Target Help button')
def click_on_target_help_button(context):
    context.driver.find_element(*HELP_BTN).click()

@when('Select Search Field')
def select_search_field(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys()  # *=multiple items

@when('Click Search button')
def click_on_search_button(context):
    context.driver.find_element(*SEARCH_BTN).click()

@when('Click on Top Help section')
def click_on_top_help(context):
    context.driver.find_elements(*TOP_HELP_SECTION).click()

@when('Click on Bottom Help section')
def click_on_bottom_help(context):
    context.driver.find_elements(*BOTTOM_HELP_SECTION)

@when('Click on Browse All Help pages')
def click_on_browse_all_help(context):
    context.driver.find_element(*BROWSE_ALL_HELP)

@then('Verify {element_amount} UI elements on the Target Help page') ##total CSS links 2-5
def verify_all_ui_element_shown(context, element_amount):
    element_amount = int(element_amount)
    elements = context.driver.find_elements(By.CSS_SELECTOR, "[class='container clearfix']")
    assert element_amount == len(elements), \
        f'Expected {element_amount} links, but got {len(elements)}'
    print('test case passed')





