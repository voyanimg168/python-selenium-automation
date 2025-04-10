from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class HelpPage(Page):
    HELP_BTN = (By.CSS_SELECTOR, "[class='custom-h2']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@class='btn-sm search-btn']")
    BROWSE_ALL_HELP = (By.CSS_SELECTOR, "[class*='boxSmall txtAC']")
    # HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    # HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    HELP_TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    CURRENT_PROMOTIONS = (By.CSS_SELECTOR, "[class='boxSmall txtAC commonLinks']")
    HELP_URL = 'https://help.target.com/help'
    HELP_RETURNS_URL = 'https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery='
    OPTION_VALUE = (By.XPATH, "//div[@class='mrgT10LeftNav']")

    #Dynamic locator => generates locator during the test run
    def _get_header_locator(self, header):
        # HEADER (By.XPATH, "//h1[text()=' {SUBSTRING}']") => (By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTRING}', header)]

    def open_help_page(self):
        self.open_url(self.HELP_URL)
        sleep(3)

    def open_help_returns_page(self):
        self.open_url(self.HELP_RETURNS_URL)
        sleep(3)

    # def click_on_view_current_promotions(self, current_promotions):
    #     self.click_on_view_current_promotions(*self.CURRENT_PROMOTIONS)

    def select_browse_help_topic(self, option_value):
        print(option_value)
        dd = self.find_element(*self.HELP_TOPIC_SELECTION_DD)
        select = Select(dd)
        select.select_by_value(option_value)
        sleep(10)

    # def verify_returns_opened(self):
    #     self.wait_until_visible(*self.HEADER_RETURNS)
    #     sleep(5)

    # def verify_promotions_opened(self):
    #     self.wait_until_visible(*self.HEADER_PROMOTIONS)

    def verify_help_topic_page_opens(self, header):
        # header = Returns / Current promotions / ...
        sleep(5)
        locator = self._get_header_locator(header)
        print(locator)
        self.wait_until_visible(*locator)

    def click_on_target_help_btn(self, help_btn):
        self.click_on_target_help_btn(*self.HELP_BTN)

    def select_search_field(self, search_field):
        self.select_search_field(*self.SEARCH_FIELD)

    def click_on_search_btn(self, search_btn):
        self.click_on_search_btn(*self.SEARCH_BTN)

    def click_on_browse_all_help(self, browse_all_help):
        self.click_on_browse_all_help(*self.BROWSE_ALL_HELP)

    def verify_all_ui_element_shown(self, element_amount):
        element_amount = int(element_amount)
        elements = self.find_elements(By.CSS_SELECTOR, "[class='container clearfix']")
        assert element_amount == len(elements), \
            f'Expected {element_amount} links, but got {len(elements)}'
