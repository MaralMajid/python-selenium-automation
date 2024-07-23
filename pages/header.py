from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class Header(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR,"#search")
    SEARCH_BTN= (By.CSS_SELECTOR,"[data-test='@web/Search/SearchButton']")

    def search(self):
        self.input_text("coffee", *self.SEARCH_FIELD)
        self.click(self.SEARCH_BTN)

        sleep(6)
