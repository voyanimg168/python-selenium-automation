from selenium.webdriver.common.by import By

from pages.base_page import Page


class CirclePage(Page):
    BENEFIT_CELLS = (By.CSS_SELECTOR, "[class='cell-item-content']")

def open_target_circle_page(self, base_url):
    self.open_target_circle_page(base_url)
    self.driver.get(f'self.base_url + /l/target-circle/-/N-pzno9')

def click_target_circle_benefit(self):
    self.click_target_circle_benefit(*self.BENEFIT_CELLS).click()

def verify_all_target_circle_benefit_cells_show(self, cell_amount):
    # cell_amount = int(cell_amount)
    # cells = context.driver.find_elements(*BENEFIT_CELLS)
    # print(cells)
    # assert len(cells) == cell_amount, f'Expected {cell_amount} cells, but got {len(cells)}'
    self.verify_all_target_circle_benefit_cells(self, cell_amount)