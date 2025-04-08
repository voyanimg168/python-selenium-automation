from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SIGNIN_ICON_HEADER = (By.XPATH, "//span[text()='Sign in']")
    SIGNIN_ICON_NAVIGATION = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']") #or [data-test='@web/CartLink']
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")  # or (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")

    def signin_icon_header(self):
        # context.driver.find_element(*SIGNIN_ICON_HEADER).click()
        # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_HEADER),
        #                           message='Search btn not clickable').click()
        # self.click(*self.SIGNIN_ICON_HEADER)
        self.wait_until_clickable_click(*self.SIGNIN_ICON_HEADER)

    def signin_icon_navigation(self):
        # context.driver.find_element(*SIGNIN_ICON_NAVIGATION).click()
        # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_ICON_NAVIGATION),
        #                           message='Search btn not clickable').click()
        # self.click(*self.SIGNIN_ICON_NAVIGATION)
        self.wait_until_clickable_click(*self.SIGNIN_ICON_NAVIGATION)

    def search_product(self, search_word):
        print(f'Searching for product:  {search_word}')
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.wait_until_clickable_click(*self.SEARCH_BTN)

    def click_cart(self):
        print('Clicking on cart icon.')
        self.click(*self.CART_ICON)

    def verify_1_header_link(self, header_link):
        print(f'Verifying 1 header link: {header_link}')
        self.verify_1_header_link(*self.HEADER_LINKS)

    def verify_all_header_links_shown(self, link_amount):
        print(f'Expecting {link_amount} header links to be shown.')
        link_amount = self.find_elements(*self.HEADER_LINKS)
        actual_count = len(*self.HEADER_LINKS)
        assert actual_count == link_amount, f"Expected {link_amount} links, but found {actual_count}"
        print('All header links are shown correctly.')

