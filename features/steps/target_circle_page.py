from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Target circle  button')
def circle_button_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()


@when('Find benefit cells shown')
def find_benefit_cells(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='cell-item-content']")

sleep(7)
@then('Verify that 10 benefit cells')
def count_benefit_cells(context):
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[class='cell-item-content']")
    assert len(cells) == 10 , f' Expected 10 cells, got {len(cells)}'