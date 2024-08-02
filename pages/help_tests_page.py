from pages.base_page import Page

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class HelpTestsPage(Page):

    HEADER_RETURNS = (By.CSS_SELECTOR, '[id="pageTitle"] h1')
    HEADER_GIFT_CARD = (By.XPATH, "//h1[text()=' Target GiftCard balance']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")


    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')


    def verify_returns(self):
        self.wait_for_element_appear(*self.HEADER_RETURNS)


    def select_topic(self):
        dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(dd)
        select.select_by_value('Gift Cards')


    def verify_gift_card(self):
        self.wait_for_element_appear(*self.HEADER_GIFT_CARD)

