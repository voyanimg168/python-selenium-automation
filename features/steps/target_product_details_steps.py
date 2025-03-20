from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "[class='styles_ndsCarouselItem__dnUkr']") # [0:3:1]
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target {product_id} page')
def open_target_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/denizen-from-levi-s-men-s-285-relaxed-fit-jeans/-/A-54551690?preselect=81782659#lnk=sametab')
    sleep(5)

@when('Click on {product_id}} color options')
def click_product_color_options(context, product_id):
    context.driver.find_elements(*COLOR_OPTIONS).send_keys()
    sleep(10)

@then('A54551690 color should change')
def click_through_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS).send_keys()
    print(color_options)

    for color_options in color_options:
        color_options.send_keys()
        print(color_options)
        color_options.find_elements(*COLOR_OPTIONS).send_keys()

        selected_color = context.driver.find_element(*SELECTED_COLOR).send_keys()
        print('Current color: ', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors}, but got {actual_colors}'

@then('A-91511634 color should change')
def click_through_colors(context):
    expected_colors = ['black/gum', 'dark khaki', 'grey', 'navy/tan', 'white/navy/red', 'white/sand/tan']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print(color_options)

    for color_options in color_options:
        color_options.send_keys()
        print(color_options)
        color_options.find_elements(*COLOR_OPTIONS).send_keys()

        selected_color = context.driver.find_element(*SELECTED_COLOR).send_keys()
        print('Current color: ', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

        assert actual_colors == expected_colors, f'Expected {expected_colors}, but got {actual_colors}'