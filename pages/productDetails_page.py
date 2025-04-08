from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductDetailsPage(Page):
    COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
    ACTUAL_COLOR = (By.CSS_SELECTOR, 'div[aria-label*="color"]')

def open_target_product_page(self, product_id):
    self.open_target_product_page(product_id)
    self.driver.get(f'self.base_url + /p/{product_id}')
    # context.driver.get(f'https://www.target.com/p/{product_id}')
    # sleep(8)

def click_through_colors(self, product_id, expected_colors):
    self.click_through_colors(product_id, expected_colors).send_keys()
    print(self.driver.find_elements(*self.ACTUAL_COLOR).text) #?????
    # sleep(15)
    #
    # expected_colors = expected_colors.split(', ')
    # actual_colors = []
    #
    # color_options = context.driver.find_elements(*COLOR_OPTIONS)
    #
    # for color in color_options:
    #     sleep(2)
    #     color.click()
    #     color_name = context.driver.find_element(*ACTUAL_COLOR).text
    #
    #     color_name = color_name.split('\n')[1]
    #     actual_colors.append(color_name)
    #
    # assert actual_colors == expected_colors, f'Error. Expected {expected_colors}, but got {actual_colors}'
