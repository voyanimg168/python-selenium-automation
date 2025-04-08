from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from features.steps.target_mainPage_steps import SEARCH_FIELD
from time import sleep
from pages.base_page import Page


class HelpPage(Page):
    HELP_BTN = (By.CSS_SELECTOR, "[class='custom-h2']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@class='btn-sm search-btn']")
    TOP_HELP_SECTION = (By.CSS_SELECTOR, "[class='container clearfix'][3]")
    BOTTOM_HELP_SECTION = (By.CSS_SELECTOR, "[class='container clearfix'][4]")
    BROWSE_ALL_HELP = (By.CSS_SELECTOR, "[class='container clearfix'][5]")
    # HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    # HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    #Dynamic locator => generates locator during the test run
    def _get_header_locator(self, header):
        # HEADER (By.XPATH, "//h1[text()=' {SUBSTRING}']") => (By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTRING}', header)]

    def open_help_page(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    # def verify_returns_opened(self):
    #     self.wait_until_visible(*self.HEADER_RETURNS)
    #     sleep(5)

    def select_topic(self, option_value):
        dd = self.find_element(*self.TOPIC_SELECTION_DD)
        select = Select(dd)
        select.select_by_value(option_value)
        sleep(10)

    # def verify_promotions_opened(self):
    #     self.wait_until_visible(*self.HEADER_PROMOTIONS)

    def verify_correct_help_page_opened(self, header):
        # header = Returns / Current promotions / ...
        locator = self._get_header_locator(header)
        print(locator)
        self.wait_until_visible(*locator)

    def open_help_page(self):
        self.open_help_page('https://help.target.com/help')

    def click_on_target_help_btn(self):
        self.click_on_target_help_btn(*self.HELP_BTN)

    def select_search_field(self):
        self.select_search_field(*self.SEARCH_FIELD).send_keys(SEARCH_FIELD)

    def click_on_search_btn(self):
        self.click_on_search_btn(*self.SEARCH_BTN)

    def click_on_top_help(self):
        self.click_on_top_help_btn(*self.TOP_HELP_SECTION)

    def click_on_bottom_help(self):
        self.click_on_bottom_help_btn(*self.BOTTOM_HELP_SECTION)

    def click_on_browse_all_help(self):
        self.click_browse_all_help_btn(*self.BROWSE_ALL_HELP)

    def verify_all_ui_element_shown(self, element_amount):
        # element_amount = int(element_amount)
        # elements = context.driver.find_elements(By.CSS_SELECTOR, "[class='container clearfix']")
        # assert element_amount == len(elements), \
        #     f'Expected {element_amount} links, but got {len(elements)}'
        self.verify_all_ui_element_shown(self, element_amount)