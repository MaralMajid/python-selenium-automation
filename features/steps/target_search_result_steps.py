from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Verify search results shown for {expected_product}')
def verify_search_worked(context, expected_product):
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-test='resultsHeading']" )))
    actual_text = context.driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'





@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    assert expected_product in context.driver.current_url, f'Expected {expected_product} not in current url {context.driver.current_url}'