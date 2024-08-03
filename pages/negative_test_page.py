from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page
from pages.header_page import Header
from pages.sign_in_page import Sign_In


class NegativeTestPage(Page):
    INPUT_EMAIL = (By.CSS_SELECTOR,"input[id='username']")
    INPUT_PASSWORD = (By.CSS_SELECTOR,"input[id='password']")
    CLICK_SIGNIN_BTN = (By.CSS_SELECTOR,"button[id='login']")
    ERROR_MSG =(By.CSS_SELECTOR, "div[data-test='authAlertDisplay'] div")



    def input_email(self):
        self.driver.find_element(*self.INPUT_EMAIL).send_keys("maralmajidli94@gmail.com")



    def input_password(self):
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys("1234abcd")



    def click_signin_btn(self):
        self.driver.find_element(*self.CLICK_SIGNIN_BTN).click()
        sleep(3)


    def verify_error_message(self):
        self.wait_for_element_appear(*self.ERROR_MSG)
        self.verify_partial_text(' find your account.', *self.ERROR_MSG)
        # error_message = self.find_element(*self.ERROR_MSG).text
        # assert "find your account" in error_message, f'Expected find your account but got {error_message}'

