from behave import when, then
from selenium.webdriver.common.by import By

EMAIL = 'lexberto@angieplease.com'
# FIRST_NAME = 'lexberto'
# LAST_NAME= 'angie'
PASSWORD = 'LEXberto'
SIGNIN_PAGE_TITLE = (By.XPATH, '//h1[text()="Sign in or create account"]')
SIGNIN_EMAIL = (By.CSS_SELECTOR, '[id*="username"]')
CONTINUE_SIGNIN_BTN = (By.CSS_SELECTOR, 'button[id*="login"]')
SIGNIN_PASSWORD = (By.CSS_SELECTOR, '[data-test="login-password"]')
SIGNIN_PASSWORD_BTN = (By.CSS_SELECTOR, 'button[id*="login"]')
# SKIP_ADD_MOBILE_PHONE = (By.CSS_SELECTOR, "[href='/']")
# CREATE_PASSKEY_LATER = (By.CSS_SELECTOR, "button[class*='styles_ndsBaseButton__W8Gl7 ']")[1]
SIGNIN_CONFIRMATION = (By.CSS_SELECTOR, "[class='styles_ndsRow__iT6yG']"[3]) # "span[class='sc-74ac6b89-0 honmwX']"  # text 'Account since <date>'
T_AND_C_LINK = (By.CSS_SELECTOR, "[href='/c/terms-conditions/-/N-4sr7l'][target='_blank']")
T_AND_C_URL = 'https://www.target.com/c/terms-conditions/-/N-4sr7l'

@when('Click on Sign In icon in Header')
def signin_icon_header(context):
    # context.driver.find_element(*SIGNIN_ICON_HEADER).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_HEADER), message='Search btn not clickable').click()
    context.app.header.signin_icon_header()

@when('Click on Sign In icon on Navigation Page')
def signin_icon_navigation(context):
    # context.driver.find_element(*SIGNIN_ICON_NAVIGATION).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_NAVIGATION), message='Search btn not clickable').click()
    context.app.header.signin_icon_navigation()

@when('Verify Sign In Form Opens')
def verify_signin_form_opens(context):
    # actual_text = context.driver.find_element(*SIGNIN_PAGE_TITLE).text
    # expected_text = 'Sign in with password'
    # assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
    context.app.login_page.verify_signin_form_opens()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window: ', context.original_window)

@when('Input signin email')
def input_signin_email(context):
    context.app.login_page.input_signin_email()

@when('Click continue signin button after email')
def click_continue_signin_btn(context):
    context.app.login_page.click_continue_signin_btn()

@when('Click Terms and Conditions link')
def click_terms_and_conditions(context):
    context.app.login_page.click_terms_and_condition()

@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()
    # sleep(1)
    # all_windows = context.driver.window_handles
    # print('All windows: ', all_windows)
    # context.driver.switch_to_window(all_windows[1])

@when('Verify Terms and Conditions page opens')
def verify_terms_and_conditions_opens(context):
    context.app.login_page.verify_terms_and_condition_opens()

@when('Close current page')
def close_current_page(context):
    context.app.base_page.close()

@when('Return to original window')
def switch_to_original_window(context):
    print('Switch back to original window', context.original_window)
    context.app.base_page.switch_to_window_by_id(context.original_window)
    # context.driver.switch_to_window(context.original_window)

@when('Input signin password')
def input_signin_password(context):
    context.app.login_page.input_signin_password()

@when('Input incorrect password')
def input_incorrect_password(context):
    context.app.login_page.input_incorrect_password()

@when('Click on Sign In With Password Button')
def click_signin_password_btn(context):
    context.app.login_page.click_signin_password_btn()

# @when('Skip add mobile phone number')
# def skip_add_mobile_phone_number(context):
#     context.app.login_page.skip_add_mobile_phone_number()
#
# @when('Maybe later create passkey')
# def maybe_later_create_passkey(context):
#     context.app.login_page.maybe_later_create_passkey()

@then('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.login_page.verify_user_is_logged_in()

