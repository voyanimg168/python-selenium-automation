from selenium.webdriver.common.by import By
from pages.base_page import Page

class AppPage(Page):
    # Locator
    PRIVACY_POLICY = (By.XPATH, '//a[text()="privacy policy"]')

    # Methods
    def open_target_app(self):
        print('Opening Target App page')
        self.open_url(f'{self.base_url}' + 'c/target-app/-/N-4th2r')

    def click_privacy_policy(self):
        print('Clicking on Privacy Policy link...')
        self.click(*self.PRIVACY_POLICY)
        self.wait_until_clickable_click(*self.PRIVACY_POLICY)

    def verify_privacy_policy_opens(self):
        print('Verifying that Privacy Policy page opens...')
        self.verify_partial_url('target-privacy-policy')
