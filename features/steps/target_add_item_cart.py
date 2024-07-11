from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Add the item to cart')
def add_to_cart(context):
    context.driver.execute_script("window.scrollBy(0, 510)")
    sleep(5)
    item = context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor82436749")
    item.click()
    sleep(6)


@then('Click on right add to cart button')
def right_side_add_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(7)


@when('Click on view cart button')
def view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[class*='ibmrHV']").click()
    sleep(6)


