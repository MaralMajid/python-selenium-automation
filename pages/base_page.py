from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15 )

    def open_url(self, url):
        self.driver.get(url)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator ):
        self.driver.find_element(*locator).click()


    def input_text(self, text,  *locator ):
        self.driver.find_element(*locator).send_keys(text)


    def get_current_window(self):
        w = self.driver.current_window_handle
        print('Current window: ', w)
        return w

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened())
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        print(f'Switched to window => {windows[1]}')

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)


    def close(self):
        self.driver.close()
        sleep (5)


    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} did not match {actual_text}'


    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text == actual_text, f'Expected {expected_partial_text} not in actual {actual_text}'



    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} did not match {actual_url}'


    def verify_partial_url(self, expected_partial_url, *locator):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in actual {actual_url}'

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} did not appear'
        )
