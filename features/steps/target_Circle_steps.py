from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, "[class='cell-item-content']")

@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@when('Click on Target Circle benefit cell')
def click_target_circle_benefit(context):
    context.driver.find_element(*BENEFIT_CELLS).click()

@then('Verify {cell_amount} benefit cells show on Target Circle page')
def verify_all_target_circle_benefit_cells_show(context, cell_amount):
    cell_amount = int(cell_amount)
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    print(cells)
    assert len(cells) == cell_amount, f'Expected {cell_amount} cells, but got {len(cells)}'
