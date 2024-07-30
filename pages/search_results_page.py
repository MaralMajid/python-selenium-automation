from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class SearchResutsPage(Page):

    SEARCH_RESULT_TXT= (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    RIGHT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="shippingButton"]')
    VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/cart']")

    def verify_search_results(self, expected_product):
        self.verify_text(expected_product, *self.SEARCH_RESULT_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def add_item_to_cart(self):
        self.driver.execute_script("window.scrollBy(0, 510)")
        sleep(5)
        self.driver.wait.until(EC.element_to_be_clickable(self.ADD_CART_BTN)).click()

    def right_side_add_button(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.RIGHT_ADD_TO_CART_BTN)).click()


    def view_cart(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.VIEW_CART_BTN)).click()