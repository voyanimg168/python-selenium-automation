from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    SEARCH_RESULTS_URL = 'https://www.target.com/s?searchTerm=tea&tref=typeahead%7Cterm%7Ctea%7C%7C%7Chistory'
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']") #or (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_RESULTS_MESSAGE = (By.CSS_SELECTOR, "[@data-test='boxEmptyMsg']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')
    SIDE_NAV_VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="product-title"]')
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_TITLE).text

    def hover_fav_icon(self):
        self.hover_element(*self.FAVORITES_BTN)
        # fav_icon = self.find_element(*self.FAVORITES_BTN)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(fav_icon)
        # actions.perform()

    def verify_fav_tooltip(self):
        self.wait_for_element_visible(*self.FAVORITES_TOOLTIP_TXT)

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)
        actual_text = self.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
        print('Search results text:', actual_text)

    def verify_expected_text_url(self, search_word, *search_results_url):
        self.verify_partial_url(search_word)
        # search_results_url = self.driver.search_results_url
        # print(search_results_url)
        # assert search_word in search_results_url, f'Expected {search_word} not found in {search_results_url}'
        # self.wait_until_visible(search_word, *self.SEARCH_RESULTS_URL)
        print("Search word found in search results url:", search_word, *search_results_url)

    def click_add_to_cart(self):
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(3)
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN).click()
        # self.find_element(*self.ADD_TO_CART_BTN)[2].click()

    def store_product_name(self):
        # self.wait_until_visible(*self.SIDE_NAV_PRODUCT_NAME)
        # self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text()
        self.store_product_name(*self.SIDE_NAV_PRODUCT_NAME)

    def side_nav_click_add_to_cart(self):
        # self.wait.until(*self.SIDE_NAV_ADD_TO_CART_BTN)
        # self.find_element(*self.SIDE_NAV_ADD_TO_CART_BTN).click()
        self.wait_until_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN).click()

    def side_nav_click_view_cart(self):
        # self.wait.until(*self.SIDE_NAV_VIEW_CART_BTN).click()
        # self.find_element(*self.SIDE_NAV_VIEW_CART_BTN).click()
        self.wait_until_clickable_click(*self.SIDE_NAV_VIEW_CART_BTN).click()

    def verify_products_name_img(self):
        # To see ALL listings (comment out if you only check top ones):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        # Find all products:
        all_products = self.find_elements(*self.LISTINGS)
        # print(all_products)
        assert len(all_products) > 0, 'No products found'

        for product in all_products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            assert title != '', 'Product title not shown'
            # print(title)
            product.find_element(*self.PRODUCT_IMG)

        # sleep(5)
        # products = self.find_elements(*self.LISTINGS)[:8]
        # print(len(products))
        #
        # for product in products:
        #     title = product.find_element(*self.PRODUCT_TITLE).text
        #     assert title, 'Product title not shown'
        #     print(title)
        #     product.find_element(*self.PRODUCT_IMG)

