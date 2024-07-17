from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ORDER_SUMMARY_TEXT = (By.CSS_SELECTOR, "[data-test='cart-summary-title']")
@then("Verify cart is empty")
def verify_cart(context):
    expected_text= 'Your cart is empty'
    actual_text= context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text in actual_text , f'Expected{expected_text} at in actual {actual_text}'


@then('Verify the item in the cart')
def verify_item(context):
    sleep(5)
    actual_text = context.driver.wait.until(EC.presence_of_element_located(ORDER_SUMMARY_TEXT))
    expected_text = 'Order summary'
    assert expected_text in actual_text.text, f'Expected{expected_text} at in actual {actual_text.text}'


