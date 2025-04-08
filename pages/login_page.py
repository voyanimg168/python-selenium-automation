from selenium.webdriver.common.by import By

from pages.base_page import Page

class LoginPage(Page):
    SIGNIN_PAGE_TITLE = (By.XPATH, '//h1[text()="Sign in or create account"]')
    SIGNIN_EMAIL = (By.CSS_SELECTOR, '[id*="username"]')
    CONTINUE_SIGNIN_BTN = (By.CSS_SELECTOR, 'button[id*="login"]')
    SIGNIN_PASSWORD = (By.CSS_SELECTOR, '[data-test="login-password"]')
    SIGNIN_PASSWORD_BTN = (By.XPATH, '//span[text()="Sign in with password"]')
    SIGNIN_CONFIRMATION = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    TERMS_AND_CONDITION = (By.XPATH, '//a[text()="terms and condition"]')

    def verify_signin_form_opens(self):
        expected_text = 'Sign in or create account'
        self.verify_text(expected_text, *self.SIGNIN_PAGE_TITLE)
        # actual_text = self.find_element(*SIGNIN_BTN).text
        # assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

    def input_signin_email(self, signin_email):
        self.input_text(*self.SIGNIN_EMAIL)

    def click_continue_signin_btn(self, continue_signin_btn):
        self.wait_until_clickable_click(*self.CONTINUE_SIGNIN_BTN).click()

    def click_terms_and_condition(self):
        print('Clicking on Terms and Condition link...')
        self.click(*self.TERMS_AND_CONDITION)
        self.wait_until_clickable_click(*self.TERMS_AND_CONDITION).click()

    def verify_terms_and_condition_opens(self):
        print('Verifying that Terms and Condition page opens...')
        self.verify_partial_url('target-terms_and_condition')

    def input_signin_password(self, signin_password):
        self.input_text(*self.SIGNIN_PASSWORD)

    def click_signin_password_btn(self, signin_password_btn):
        self.wait_until_clickable_click(*self.SIGNIN_PASSWORD_BTN).click()

    def verify_user_is_logged_in(self, signin_confirmation):
        self.verify_text(*self.SIGNIN_CONFIRMATION)