from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on Sign In icon on Main Page')
def signIn_icon_mainPage(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(2)
@when('Click on Sign In icon on Navigation Page')
def signIn_icon_navigationPage(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()


@then('Verify Sign In Form Opens')
def verify_signIn_form_opens(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "button[id='login']").text
    expected_text = 'Sign in with password'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
    print('Test case passed')
