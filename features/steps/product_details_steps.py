from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#COLOR_OPTIONS_HAT = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
COLOR_OPTIONS = (By.CSS_SELECTOR,'div[aria-label="Carousel"] img')
SELECTED_COLOR = (By.CSS_SELECTOR,"div[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)



@then('Verify user can click through colors of umbrella')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Gray', 'Moss Green', 'Rose Pink', 'Glowing', 'Towers', 'Walker', 'Escape', 'Sites', 'Touring', 'Marietta']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        print('Current color', selected_color)
        actual_colors.append(selected_color)
        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'





@then('Verify user can click through colors of watch')
def click_and_verify_colors(context):
    expected_colors = ['silver', 'gunmetal']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        print('Current color', selected_color)
        actual_colors.append(selected_color)
    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'





