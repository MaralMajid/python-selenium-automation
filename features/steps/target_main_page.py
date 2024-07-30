from selenium.webdriver.common.by import By
from behave import given, when
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



@given('Open Target main page')
def open_target(context):
    context.app.main_page.open()

@when("Click on cart button")
def click_card(context):
    context.app.header.click_cart()

@when ("Click on Sign in button")
def click_sign_in(context):
    context.app.header_page.sign_in_button()
    #context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-test='@web/AccountLink']")))
    #context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

@when("Click on right Sign in button")
def click_right_button(context):
    context.app.header_page.right_sign_in_button()
    # context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-test='accountNav-signIn']")))
    # context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()



@when('Search for {product}')
def search_for_product(context,product):
    context.app.header.search_for_product(product)






