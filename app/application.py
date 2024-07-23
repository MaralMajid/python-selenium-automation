from webbrowser import Chrome

from pages.header import Header
from pages.main_page import MainPage
from pages.search_results import SearchResutsPage
from pages.base_page import Page

class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.main_page = MainPage(driver)
        self.search_page = SearchResutsPage(driver)
        self.header = Header(driver)


