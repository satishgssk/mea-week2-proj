from behave import *

@given('Behave has been successfully installed')
def step_impl(context):
    pass

@when('We run our first test')
def step_impl(context):
    assert True is not False

@then('Behave should test it correctly')
def step_impl(context):
    assert context.failed is False
