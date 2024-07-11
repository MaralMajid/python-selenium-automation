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


@when ("Click on Sign in button")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    sleep(2)

@when("Click on right Sign in button")
def click_right_button(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(2)


@when('Search for {product}')
def search_for_product(context,product):
    context.driver.find_element(By.CSS_SELECTOR,"#search" ).send_keys(product)



@when('Click search button')
def click_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/Search/SearchButton']").click()
    sleep(6)


