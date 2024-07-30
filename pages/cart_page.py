from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")
    CART_ORDER_SUMMARY_MSG = (By.CSS_SELECTOR, "[data-test='cart-summary-title']")

    def verify_cart_empty(self):
        self.verify_text( 'Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_order_in_cart(self):
        self.verify_text('Order summary', *self.CART_ORDER_SUMMARY_MSG)

