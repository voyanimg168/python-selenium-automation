from behave import given, when, then

@given('Open Help page')
def open_help_page(context):
    context.app.help_page.open_help_page()

# @when('Select Help topic {option_value}')
# def select_topic(context, option_value):
#     context.app.help_page.select_topic(option_value)

# @then('Verify help Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
#
# @then('Verify help Current Promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()

# @then('Verify help {header} page opened')
# def verify_correct_help_page_opened(context, header):
#     context.app.help_page.verify_returns_opened(header)

