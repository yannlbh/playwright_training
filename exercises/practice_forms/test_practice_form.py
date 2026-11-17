import pytest
from playwright.sync_api import Page, expect
from exercises.practice_forms.form_page import FormPage

VALID_COUNTRY = "United States"
VALID_TITLE = "Mr."
VALID_FIRST_NAME = "John"
VALID_LAST_NAME = "Smith"
VALID_DOB = "2002-01-01"
VALID_DOJ = "17/10/2026"
VALID_EMAIL = "validemail@gmail.com"
VALID_PHONE_CODE = "+1"
VALID_PHONE_NUMBER = "555-123-4567"

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
    expect(init_form_page.success_submit_message).to_contain_text("Details Successfully Added!")


def test_TC02_empty_form(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Leave all fields empty
      2. Click Submit

    Expected: A "required" error appears under each mandatory field.
    """
    pass


def test_TC03_invalid_email(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Fill all fields correctly except email = "notanemail"
      2. Click Submit

    Expected: Error "Invalid Email Address" is shown.

    """
    pass


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
    pass


def test_TC05_missing_comm_pref(init_form_page):
    """

    :param init_form_page:
    :return:

    Steps:
      1. Fill all fields but select no radio
      2. Click Submit

    Expected: Error "Please select a Communication Preference" is shown.

    """
    pass


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
