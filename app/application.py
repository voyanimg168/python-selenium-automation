from pages.app_page import AppPage
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.help_page import HelpPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.productDetails_page import ProductDetailsPage
from pages.searchResults_page import SearchResultsPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.productDetails_page = ProductDetailsPage(driver)
        self.searchResults_page = SearchResultsPage(driver)
        self.app_page = AppPage(driver)

# app = Application()
# app.header.search()
# app.search_results_page.verify_search_results()