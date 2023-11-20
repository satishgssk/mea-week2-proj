import time, json
from behave import given, when, then
from selenium.webdriver.common.by import By
from hamcrest import equal_to, assert_that

@given('That a user is on the url "{url}"')
def url(context, url):
    context.browser.get(url)

@when('The user enters the item name "{name}", description "{description}", and price "{price}" into the CREATE section')
def step_enter_post_data(context, name, description, price):
    context.browser.find_element(By.ID, 'inputName').send_keys(name)
    context.browser.find_element(By.ID, 'inputDescription').send_keys(description)
    context.browser.find_element(By.ID, 'inputPrice').send_keys(float(price))

@when('The user enters the item _id "{_id}" into the GET ONE section')
def step_enter_get_one_data(context, _id):
    context.browser.find_element(By.ID, 'inputID').send_keys(_id)

@when('The user enters the item _id "{_id}", name "{name}", description "{description}", and price "{price}" into the UPDATE section')
def step_enter_update_data(context, _id, name, description, price):
    context.browser.find_element(By.ID, 'inputUpdateID').send_keys(_id)
    context.browser.find_element(By.ID, 'inputUpdateName').send_keys(name)
    context.browser.find_element(By.ID, 'inputUpdateDescription').send_keys(description)
    context.browser.find_element(By.ID, 'inputUpdatePrice').send_keys(float(price))

@when('The user enters the item _id "{_id}" into the DELETE section')
def step_enter_delete_data(context, _id):
    context.browser.find_element(By.ID, 'inputDeleteID').send_keys(_id)

@when('The user clicks the POST button')
def step_click_post_button(context):
    context.browser.find_element(By.ID, 'buttonCreate').click()

@when('The user clicks the GET One button')
def step_click_get_one_button(context):
    context.browser.find_element(By.ID, 'buttonReadOne').click()

@when('The user clicks the PUT button')
def step_click_put_button(context):
    context.browser.find_element(By.ID, 'buttonUpdate').click()

@when('The user clicks the DELETE button')
def step_click_delete_button(context):
    context.browser.find_element(By.ID, 'buttonDelete').click()

@then('The READ ALL section will populate with JSON containing _id "{_id}", name "{name}", description "{description}", and price "{price}"')
def step_check_for_created_item_json(context, _id, name, description, price):
    expected = json.dumps({"_id":int(_id),"description":description,"name":name,"price":float(price)},separators=(',', ':'))
    time.sleep(2)
    actual = context.browser.find_element(By.ID, 'listOutput').text
    assert_that(actual, equal_to(expected))

@then('The READ ONE section will populate with JSON containing _id "{_id}", name "{name}", description "{description}", and price "{price}"')
def step_check_for_read_one_item_json(context, _id, name, description, price):
    expected = json.dumps({"_id":int(_id),"description":description,"name":name,"price":float(price)},separators=(',', ':'))
    time.sleep(2)
    actual = context.browser.find_element(By.ID, 'singleOutput').text
    assert_that(actual, equal_to(expected))

@then('The READ ONE section will be empty')
def step_check_for_delete(context):
    expected = '[]'
    time.sleep(2)
    actual = context.browser.find_element(By.ID, 'singleOutput').text
    assert_that(actual, equal_to(expected))