from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify cart is empty")
def verify_cart(context):
    expected_text= 'Your cart is empty'
    actual_text= context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text in actual_text , f'Expected{expected_text} at in actual {actual_text}'


@then('Verify the item in the cart')
def verify_item(context):
    expected_text = 'Order summary'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-summary-title']").text
    assert expected_text in actual_text, f'Expected{expected_text} at in actual {actual_text}'
    sleep(7)
