from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

TERM_COND_LINK = (By.CSS_SELECTOR, "a[aria-label='terms & conditions - opens in a new window']")

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_terms_conditions_page.get_current_window()
    print(context.original_window)


@when('Click on Target terms and conditions link')
def click_term_condition_link(context):
    context.app.target_terms_conditions_page.click_term_condition_link()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.target_terms_conditions_page.switch_to_new_window()


@then ('Verify Terms and Conditions page is opened')
def verify_termcondition_url (context):
    context.app.terms_and_conditions_page.verify_tc_url()




@then('User can close new window')
def close_new_window(context):
    context.app.terms_and_conditions_page.close()


@then('Switch back to original')
def switch_back_original_window(context):
    context.app.target_terms_conditions_page.switch_to_window_by_id(context.original_window)