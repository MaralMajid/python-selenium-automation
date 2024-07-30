from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CART_ORDER_SUMMARY_MSG = (By.CSS_SELECTOR, "[data-test='cart-summary-title']")
@then("Verify cart is empty")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify the item in the cart')
def verify_item(context):
    context.app.cart_page.verify_order_in_cart()

