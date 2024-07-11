from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Target circle  button')
def circle_button_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()


@when('Find benefit cells shown')
def find_benefit_cells(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='cell-item-content']")



@then('Verify benefit has {number} links')
def count_benefit_cells(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class='cell-item-content']")
    assert len(links) == number , f' Expected {number}, got {len(links)}'
    sleep(5)