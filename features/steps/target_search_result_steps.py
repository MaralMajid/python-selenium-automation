from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify search results shown for {expected_product}')
def verify_search_worked(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'
    sleep(2)




@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    assert expected_product in context.driver.current_url, f'Expected {expected_product} not in current url {context.driver.current_url}'