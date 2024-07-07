from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("Click on cart button")
def click_card(context):
    context.driver.find_element(By.CSS_SELECTOR,"use[href='/icons/Cart.svg#Cart']").click()
    sleep(8)

@then("Verify cart is empty")
def verify_cart(context):
    expected_text= 'Your cart is empty'
    actual_text= context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text in actual_text , f'Expected{expected_text} at in actual {actual_text}'


@when ("Click on Sign in button")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    sleep(2)

@when("Click on right Sign in button")
def click_right_button(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(2)

@then("Verify Sign in page")
def verify_sign_in(context):
    expected_text= 'Sign into your Target account'
    actual_text=context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
    assert expected_text in actual_text, f'Expected{expected_text} at in actual {actual_text}'
