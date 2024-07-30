from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Add the item to cart')
def add_to_cart(context):
    context.app.search_page.add_item_to_cart()



@then('Click on right add to cart button')
def right_side_add_button(context):
    context.app.search_page.right_side_add_button()





@when('Click on view cart button')
def view_cart(context):
    context.app.search_page.view_cart()


