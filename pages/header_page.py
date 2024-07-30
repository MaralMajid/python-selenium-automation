from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID,"search")
    SEARCH_BTN= (By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.XPATH, "//*[@data-test='@web/AccountLink']")
    RIGHT_SIGN_IN_BTN = (By.XPATH, "//*[@data-test='accountNav-signIn']")
    def search_for_product(self,search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

        sleep(6)

    def click_cart(self):
        self.click(*self.CART_BTN)

    def sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)

    def right_sign_in_button(self):
        self.click(*self.RIGHT_SIGN_IN_BTN)
