from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
#COLOR_OPTIONS = (By.CSS_SELECTOR, "[class='styles_fadeInPicture__X_1Zl styles_animated__7ypei styles_fullWidth__z04mu styles_fullHeight__xxwBI'][alt]")
#ACTUAL_COLOR = ("[data-test='@web/VariationComponent'] div")
ACTUAL_COLOR = (By.CSS_SELECTOR, 'div[aria-label*="olor"]')

@given('Open target {product_id} page')
def open_target_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')

@then('Click on {product_id} for {expected_colors} options')
def click_through_colors(context, product_id, expected_colors):
    sleep(15)

    expected_colors = expected_colors.split(', ')
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    for color in color_options:
        sleep(2)
        color.click()
        color_name = context.driver.find_element(*ACTUAL_COLOR).text

        color_name = color_name.split('\n')[1]
        actual_colors.append(color_name)

    assert actual_colors == expected_colors, f'Error. Expected {expected_colors}, but got {actual_colors}'

