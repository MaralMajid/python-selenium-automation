from behave import then, when, given



@given('Open Help pages for Returns')
def click_cart(context):
    context.app.help_tests_page.open_help_returns()


@then('Verify Help Returns page opened')
def verify_help_page_header_returns(context):
    context.app.help_tests_page.verify_returns()


@when('Select Help topic Gift Cards')
def select_topic(context):
    context.app.help_tests_page.select_topic()


@then('Verify Help Target GiftCard balance page opened')
def verify_help_page_gift_card(context):
    context.app.help_tests_page.verify_gift_card()
