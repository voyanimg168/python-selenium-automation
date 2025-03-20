from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIGNIN_ICON_MAIN = (By.XPATH, "//span[text()='Sign in']")
SIGNIN_ICON_NAVIGATION = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
SIGNIN_BTN = (By.CSS_SELECTOR, "button[id='login']")

# @given('Open target main page')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')

@when('Click on Sign In icon on Main Page')
def signIn_icon_mainPage(context):
#   context.driver.find_element(*SIGNIN_ICON_MAIN).click()
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_MAIN), message='Search btn not clickable').click()

@when('Click on Sign In icon on Navigation Page')
def signIn_icon_navigationPage(context):
#   context.driver.find_element(*SIGNIN_ICON_NAVIGATION).click()
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_NAVIGATION), message='Search btn not clickable').click()

@then('Verify Sign In Form Opens')
def verify_signIn_form_opens(context):
    actual_text = context.driver.find_element(*SIGNIN_BTN).text
    expected_text = 'Sign in with password'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
    print('Test case passed')
