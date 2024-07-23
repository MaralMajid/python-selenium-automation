from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class SearchResutsPage(Page):
    SEARCH_RESULT_TXT= (By.XPATH, "//div[@data-test='resultsHeading']")
    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT_TXT).text
        assert 'coffee' in actual_text, f'Expected coffee not in actual {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'coffee' in url, f'Expected "coffee" not  in {url}'