from webbrowser import Chrome

from pages.header_page import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResutsPage
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.sign_in_page import Sign_In
from pages.target_signin_tc_page import TargetSinginTC
from pages.terms_and_conditions_page import TermAndConditionPage
from pages.help_tests_page import HelpTestsPage
from pages.negative_test_page import NegativeTestPage

class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.search_page = SearchResutsPage(driver)
        self.header_page = Header(driver)
        self.sign_in_page = Sign_In(driver)
        self.target_terms_conditions_page = TargetSinginTC(driver)
        self.terms_and_conditions_page = TermAndConditionPage(driver)
        self.help_tests_page = HelpTestsPage(driver)
        self.negative_test_page = NegativeTestPage(driver)


