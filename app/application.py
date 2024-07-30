from webbrowser import Chrome

from pages.header_page import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResutsPage
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.sign_in_page import Sign_In

class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.search_page = SearchResutsPage(driver)
        self.header_page = Header(driver)
        self.sign_in_page = Sign_In(driver)


