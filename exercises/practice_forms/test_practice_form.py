from time import sleep

import pytest
from playwright.sync_api import Page, expect
from exercises.practice_forms.form_page import FormPage

# region Entry values
VALID_COUNTRY = "United States"
VALID_TITLE = "Mr."
VALID_FIRST_NAME = "John"
VALID_LAST_NAME = "Smith"
VALID_DOB = "2002-01-01"
VALID_DOJ = "17/10/2026"
VALID_EMAIL = "validemail@gmail.com"
VALID_PHONE_CODE = "+1"
VALID_PHONE_NUMBER = "555-123-4567"
#endregion

#region Success / errors messages
SUCCESS_MESSAGE_SUBMIT = "Details Successfully Added!"
ERROR_MESSAGE_COUNTRY = "Country of Residence is required"
ERROR_MESSAGE_TITLE = "Title is required"
ERROR_MESSAGE_FIRST_NAME = "First Name is required"
ERROR_MESSAGE_LAST_NAME = "Last Name is required"
ERROR_MESSAGE_DOB = "Date of Birth is required"
ERROR_MESSAGE_DOJ = "Date of Joining is required (dd/mm/yyyy)"
ERROR_MESSAGE_EMAIL = "Email Address is required"
ERROR_MESSAGE_PHONE_NUMBER = "Phone Number is required"
ERROR_MESSAGE_PREF_COMM_METHOD = "Please select a Communication Preference"
#endregion

@pytest.fixture
def init_form_page(page:Page):
    form_page = FormPage(page)
    form_page.open_form_page()
    return form_page


def test_TC01_valid_form(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Fill every field with valid values
      2. Select a communication preference
      3. Click Submit

    Expected: Success message "Details Successfully Added!" is shown.
    """
    init_form_page.fill_form(VALID_COUNTRY, VALID_TITLE, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_DOB, VALID_DOJ, VALID_EMAIL, VALID_PHONE_CODE, VALID_PHONE_NUMBER,True)
    init_form_page.submit()
    expect(init_form_page.success_submit_message).to_contain_text(SUCCESS_MESSAGE_SUBMIT)

def test_TC02_empty_form(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Leave all fields empty
      2. Click Submit

    Expected: A "required" error appears under each mandatory field.
    """
    init_form_page.fill_form()
    init_form_page.submit()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_COUNTRY)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_TITLE)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_FIRST_NAME)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_LAST_NAME)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_DOB)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_DOJ)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_EMAIL)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_PHONE_NUMBER)).to_be_visible()
    expect(init_form_page.get_error_message_locator(ERROR_MESSAGE_PREF_COMM_METHOD)).to_be_visible()



def test_TC03_invalid_email(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Fill all fields correctly except email = "notanemail"
      2. Click Submit

    Expected: Error "Invalid Email Address" is shown.

    """
    init_form_page.page.locator("form").evaluate("form=>form.noValidate = true")
    init_form_page.fill_form(VALID_COUNTRY, VALID_TITLE, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_DOB, VALID_DOJ,
                             "notanemail@", VALID_PHONE_CODE, VALID_PHONE_NUMBER, True)
    init_form_page.submit()
    expect(init_form_page.get_error_message_locator("Invalid Email Address")).to_be_visible()

def test_TC04_invalid_doj(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Enter Date of Joining as 2021-06-01 (wrong format)
      2. Fill the rest validly
      3. Click Submit

    Expected: Error "Date of Joining format should be dd/mm/yyyy" is shown.
    """
    init_form_page.fill_form(VALID_COUNTRY, VALID_TITLE, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_DOB, "2021-06-01", VALID_EMAIL, VALID_PHONE_CODE, VALID_PHONE_NUMBER,True)
    init_form_page.submit()
    expect(init_form_page.get_error_message_locator("Date of Joining format should be dd/mm/yyyy")).to_be_visible()

def test_TC05_missing_comm_pref(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Fill all fields but select no radio
      2. Click Submit

    Expected: Error "Please select a Communication Preference" is shown.

    """
    init_form_page.fill_form(VALID_COUNTRY, VALID_TITLE, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_DOB, VALID_DOJ,
                             VALID_EMAIL, VALID_PHONE_CODE, VALID_PHONE_NUMBER)
    init_form_page.submit()
    expect(init_form_page.get_error_message_locator("Please select a Communication Preference")).to_be_visible()

def test_TC06_country_dropdown_op(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Open the Country dropdown

    Expected: Options include United States, Canada, United Kingdom, India, Australia, Other.

    """
    pass

def test_TC07_clear_form(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Fill several fields
      2. Click Clear

    Expected: All fields return to their empty/default state.

    """
    pass

def test_TC08_exlusive_radio_button(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Select Email, then select Phone

    Expected: Only Phone stays selected; the two radios are mutually exclusive.

    """
    pass
