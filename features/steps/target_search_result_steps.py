from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Verify search results shown for {expected_product}')
def verify_search_worked(context, expected_product):
    context.app.search_page.verify_text(expected_product)




@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    context.app.search_page.verify_url(expected_product)