from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import when, then

@when('Input wrong email address')
def input_email(context):
    context.app.negative_test_page.input_email()


@when('Input wrong password')
def input_password(context):
    context.app.negative_test_page.input_password()


@then('Click login button')
def click_login_button(context):
    context.app.negative_test_page.click_signin_btn()

@then('Verifies that error message is shown')
def verify_error_message(context):
    context.app.negative_test_page.verify_error_message()