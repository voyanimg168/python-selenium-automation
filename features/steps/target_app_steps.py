from behave import given, when, then
from time import sleep

@given('Open Target App page')
def open_target_app(context):
    print('Open Target App page')
    context.app.app_page.open_target_app()

# @given('Store original window')
# def store_original_window(context):
#     context.original_window = context.app.base_page.get_current_window_handle()
#     print('Original window: ', context.original_window)

@when('Click Privacy Policy link')
def click_privacy_policy(context):
    context.app.app_page.click_privacy_policy()

# @when('Switch to new window')
# def switch_to_new_window(context):
#     context.app.base_page.switch_to_new_window()
    # sleep(1)
    # all_windows = context.driver.window_handles
    # print('All windows: ', all_windows)
    # context.driver.switch_to_window(all_windows[1])

@then('Verify Privacy Policy page opens')
def verify_privacy_policy_opens(context):
    assert context.app.app_page.verify_privacy_policy_opens()

# @then('Close current page')
# def close_current_page(context):
#     context.app.base_page.close()
#
# @then('Return to original window')
# def switch_to_original_window(context):
#     print('Switch back to original window', context.original.window)
#     context.app.base_page.switch_to_window_by_id(context.original.window)
#     # context.driver.switch_to_window(context.original_window)
