from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    BASE_URL = 'https://www.target.com'
    SEARCH_FIELD = (By.ID, 'search_word')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")  #or (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")

    def open_main_page(self):
        self.open_url(self.base_url)
        # self.wait_until_clickable(*self.SEARCH_FIELD)
        # self.wait_until_visible(*self.SEARCH_FIELD)

