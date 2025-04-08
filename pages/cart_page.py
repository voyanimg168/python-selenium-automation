from selenium.webdriver.common.by import By
from features.steps.target_cart_steps import CART_ITEM_TITLE, CART_SUMMARY
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")  # Example XPath
    CART_ICON = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    CART_SUMMARY = (By.CSS_SELECTOR, '[class*="h-margin-b-tight"] span')  # or (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_product_name(self, cart_item_title):
        self.verify_product_name(*CART_ITEM_TITLE)
        # product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
        # print('Name in cart: ' + product_name_in_cart)
        # print('Name we have stored: ' + context.product_name)
        # assert context.product_name[:40] == product_name_in_cart[:40], \
        #     f'Expected {context.product_name[:40]} did not match {product_name_in_cart[:40]}'

    def verify_cart_amount_items(self, cart_summary):
        self.verify_cart_amount_items(CART_SUMMARY)
        # context.driver.wait.until(
        #     EC.visibility_of_element_located(CART_SUMMARY),
        #     message='Cart summary is not visible.'
        # )
        # cart_summary = context.driver.find_element(*CART_SUMMARY).text
        # assert amount in cart_summary, f'Expected {amount} items not in {cart_summary}'

    def verify_cart_empty(self, cart_empty_msg):
        # self.verify_cart_empty(f'Your cart is empty')
        # expected_text = f'Your cart is empty'
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)
        # actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
        # expected_text = 'Your cart is empty'
        # actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        # assert expected_text in actual_text, f'Expected {expected_text} did not match {actual_text}'

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart') # 'https://www.target.com/' + 'cart'
        # self.wait_until_visible(*self.base_url)
        self.wait_until_clickable_click(*self.CART_ICON)
