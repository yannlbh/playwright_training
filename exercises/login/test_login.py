from time import sleep
import pytest
from playwright.sync_api import Page, expect
from exercises.login.login_page import LoginPage

VALID_EMAIL = "user@premiumbank.com"
VALID_PASSWORD = "Bank@123"

@pytest.fixture
def init_login_page(page:Page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    return login_page

def test_tc01_valid_login(init_login_page):
    """
    :param init_login_page:
    :return: null
    Steps:
      1. Enter user@premiumbank.com in the email field
      2. Enter Bank@123 in the password field
      3. Click Sign in

    Expected: A success message "Login Successful! Welcome to Premium Banking." is shown.

    """
    init_login_page.login(VALID_EMAIL, VALID_PASSWORD) #login with the good credentials
    expect(init_login_page.success_login_message).to_be_visible() #check the success message

def test_tc02_invalid_login_empty_fields(init_login_page):
    """

    :param init_login_page:
    :return:

    Steps:
      1. Leave email and password empty
      2. Click Sign in

    Expected: Error "Email and Password are required" is shown.
    """
    init_login_page.login("", "")  # login with the email and password empty
    expect(init_login_page.error_login_message).to_contain_text("Email and Password are required")  # check the error message

