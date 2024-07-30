from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.sign_in_page import Sign_In
from time import sleep



class TargetSinginTC(Page):
    TERM_COND_LINK =(By.CSS_SELECTOR,"a[aria-label='terms & conditions - opens in a new window']")


    def click_term_condition_link(self):
        self.click(*self.TERM_COND_LINK)
        sleep(5)

    def close_new_window(self):
        self.driver.close()
