from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from features.steps.target_loginPage_steps import SIGNIN_CONFIRMATION
from pages.base_page import Page

class LoginPage(Page):
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
    SIGNIN_CONFIRMATION = (By.CSS_SELECTOR, "[id='account-sign-in']") # text 'Account since <date>'
    T_AND_C_LINK = (By.CSS_SELECTOR, "[href='/c/terms-conditions/-/N-4sr7l'][target='_blank']")
    T_AND_C_URL = 'https://www.target.com/c/terms-conditions/-/N-4sr7l'

    def verify_signin_form_opens(self):
        expected_text = 'Sign in or create account'
        self.verify_text(expected_text, *self.SIGNIN_PAGE_TITLE)
        # actual_text = self.find_element(*SIGNIN_BTN).text
        # assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

    def input_signin_email(self):
        self.wait_until_visible(*self.SIGNIN_EMAIL)
        self.input_text(self.EMAIL, *self.SIGNIN_EMAIL)

    def click_continue_signin_btn(self):
        self.wait_until_clickable_click(*self.CONTINUE_SIGNIN_BTN)

    def click_terms_and_condition(self):
        print('Clicking on Terms and Condition link...')
        sleep(3)
        self.driver.execute_script('window.scrollTo(0, 500)')
        self.wait_until_clickable_click(*self.T_AND_C_LINK)
        sleep(10)

    def verify_terms_and_condition_opens(self):
        print('Verifying that Terms and Condition page opens...')
        self.verify_partial_url('terms-conditions')
        sleep(10)

    def close_current_page(self):
        self.close()

    def input_signin_password(self):
        self.wait_until_visible(*self.SIGNIN_PASSWORD)
        self.input_text(self.PASSWORD, *self.SIGNIN_PASSWORD)

    def click_signin_password_btn(self):
        self.wait_until_clickable_click(*self.SIGNIN_PASSWORD_BTN)

    # def skip_add_mobile_phone_number(self):
    #     self.click(*self.SKIP_ADD_MOBILE_PHONE)
    #
    # def maybe_later_create_passkey(self):
    #     self.click(*self.CREATE_PASSKEY_LATER)

    def verify_user_is_logged_in(self):
        self.find_element(*self.SIGNIN_CONFIRMATION)
        # actual_text = self.find_element(*SIGNIN_CONFIRMATION).text
        # assert expected_text == actual_text, f'Expected text {expected_text} did not match {actual_text}'
        print('User logged in...')

    # def verify_search_results(self, expected_text):
    #     self.find_element(expected_text)