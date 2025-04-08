from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SIGNIN_ICON_HEADER = (By.XPATH, "//span[text()='Sign in']")
SIGNIN_ICON_NAVIGATION = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
SIGNIN_PAGE_TITLE = (By.CSS_SELECTOR, '//h1[text()="Sign in or create account"]')
SIGNIN_EMAIL = (By.CSS_SELECTOR, '[id*="username"]')
CONTINUE_SIGNIN_BTN = (By.CSS_SELECTOR, 'button[id*="login"]')
SIGNIN_PASSWORD = (By.CSS_SELECTOR, '[data-test="login-password"]')
SIGNIN_PASSWORD_BTN = (By.XPATH, '//span[text()="Sign in with password"]')
SIGNIN_CONFIRMATION = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')

@when('Click on Sign In icon in Header')
def signin_icon_header(context):
    # context.driver.find_element(*SIGNIN_ICON_HEADER).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_HEADER), message='Search btn not clickable').click()
    context.app.main_page.signin_icon_header()

@when('Click on Sign In icon on Navigation Page')
def signin_icon_navigation(context):
    # context.driver.find_element(*SIGNIN_ICON_NAVIGATION).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_NAVIGATION), message='Search btn not clickable').click()
    context.app.main_page.signin_icon_navigation()

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
def input_signin_email(context, signin_email):
    context.app.login_page.input_signin_email()

@when('Click continue signin button after email')
def click_continue_signin_btn(context, continue_signin_btn):
    context.app.login_page.click_continue_signin_btn()

@when('Click Terms and Conditions link')
def click_terms_and_conditions(context):
    context.app.login_page.click_terms_and_conditions()

@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()
    # sleep(1)
    # all_windows = context.driver.window_handles
    # print('All windows: ', all_windows)
    # context.driver.switch_to_window(all_windows[1])

@when('Verify Terms and Conditions page opens')
def verify_terms_and_conditions_opens(context):
    assert context.app.login_page.verify_terms_and_conditions_opens()

@when('Close current page')
def close_current_page(context):
    context.app.base_page.close()

@when('Return to original window')
def switch_to_original_window(context):
    print('Switch back to original window', context.original.window)
    context.app.base_page.switch_to_window_by_id(context.original.window)
    # context.driver.switch_to_window(context.original_window)

@when('Input signin password')
def input_signin_password(context, signin_password):
    context.app.login_page.input_signin_password()

@when('Click on Sign In With Password Button')
def click_signin_password_btn(context, signin_password_btn):
    context.app.login_page.click_signin_password_btn()

@then('Verify user is logged in')
def verify_user_is_logged_in(context, signin_confirmation):
    context.app.login_page.verify_user_is_logged_in()

