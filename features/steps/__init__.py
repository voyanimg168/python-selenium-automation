from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open target main page')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')

@when('Action')
def action(context):
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, '').click()

@then('Verify ')
def verify_correct_message(context):
    sleep(2)
    actual_text = context.driver.find_element(By.XPATH, "").text
    expected_text = 'Text'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'