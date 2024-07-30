from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Sign_In(Page):
    SIGN_IN_ACCOUNT = (By.XPATH,"//span[text()='Sign into your Target account']")

    def verify_sign_in_account(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_ACCOUNT)
