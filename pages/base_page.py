from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from script.target_search_script import actual_text
from support.logger import logger

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.target.com/'
        self.wait = WebDriverWait(self.driver, timeout=10)

    # menu = driver.find_element(*MENU)
    # actions = ActionChains(driver)
    # actions.move_to_element(menu)
    # actions.click(menu)
    # actions.perform()

    def open_url(self, url):
        logger.info('Opening url {url}') #supports only 1 string; use python format
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking by {locator}...')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Entering text {text} by {locator}...')
        self.driver.find_element(*locator).send_keys(text)

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by {locator}'
        )

    def wait_until_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by {locator}'
        )

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(
            EC.new_window_is_opened(),
            message=f'New window was not opened by {self.driver.current_window_handle}'
        )
        all_windows = self.driver.window_handles
        print('Current windows ', all_windows)
        print('Switching to window: ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print('Switching to window: ', window_id)

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def verify_text(self, expected_text, *locator):
        self.wait.until(
            EC.text_to_be_present_in_element(locator),
            message=f'Expected text {expected_text} does not match {actual_text}'
        )
        # actual_text = self.find_element(*locator).text
        # assert expected_text == actual_text, f'Expected text {expected_text} did not match {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        self.wait.until(
            EC.text_to_be_present_in_element(locator),
            message=f'Expected text {expected_text} not found in {actual_text}'
        )
        # actual_text = self.find_element(*locator).text
        # assert expected_text in actual_text, f'Expected text "{expected_text}" not found in {actual_text}'

    def verify_url(self, expected_url):
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f'URL does not match {expected_url}'
        )
        # current_url = self.driver.current_url
        # print(f'Current_url {current_url}')
        # assert expected_url in current_url, f'Expected {expected_url} does not match {current_url}'

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'URL not found in {expected_partial_url}'
        )
        # current_url = self.driver.current_url
        # print(f'Current url {current_url}')
        # assert expected_partial_url in current_url, f'Expected {expected_partial_url} not found in {current_url}'

    def close(self):
        self.driver.close()

