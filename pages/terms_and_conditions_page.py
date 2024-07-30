from pages.base_page import Page


class TermAndConditionPage(Page):
    def verify_tc_url(self):
        self.verify_partial_url('https://www.target.com/c/terms-conditions')

