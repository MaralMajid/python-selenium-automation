from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify Sign in page")
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_account
    # expected_text= 'Sign into your Target account'
    # actual_text=context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
    # assert expected_text in actual_text, f'Expected{expected_text} at in actual {actual_text}'
