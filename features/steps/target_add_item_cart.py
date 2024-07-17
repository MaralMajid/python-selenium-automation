from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button[data-test="orderPickupButton"]')
VIEW_CART_BTN = (By.CSS_SELECTOR, 'a[href="/cart"]')

@when('Add the item to cart')
def add_to_cart(context):
    context.driver.execute_script("window.scrollBy(0, 510)")
    sleep(5)
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[id*='addToCartButton']")))
    item = context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']")
    item.click()



@then('Click on right add to cart button')
def right_side_add_button(context):
    sleep(10)
    cart_button = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN))
    cart_button.click()





@when('Click on view cart button')
def view_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(VIEW_CART_BTN))
    item = context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']")
    item.click()




