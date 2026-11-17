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

def test_tc03_invalid_login_empty_password(init_login_page):
    """

    :param init_login_page:
    :return:

    Steps:
      1. Enter a valid email
      2. Leave password empty
      3. Click Sign in

    Expected: Error "Password is required" is shown.
    """
    init_login_page.login(VALID_EMAIL, "")  # login with valid email and no password
    expect(init_login_page.error_login_message).to_contain_text("Password is required")  # check the error message

def test_tc04_invalid_login_empty_email(init_login_page):
    """

    :param init_login_page:
    :return:

    Steps:
      1. Leave email empty
      2. Enter any password
      3. Click Sign in

    Expected: Error "Email is required" is shown.
    """
    init_login_page.login("", VALID_PASSWORD)  # login with no email and valid password
    expect(init_login_page.error_login_message).to_contain_text("Email is required")  # check the error message

def test_tc05_invalid_login_invalid_credential(init_login_page):
    """

    :param init_login_page:
    :return:

    Steps:
      1. Enter wrong@example.com
      2. Enter a wrong password
      3. Click Sign in

    Expected: Error "Invalid email id and password" is shown; no success message.
    """
    init_login_page.login("wrong@email", "wrong password")  # login with wrong email and password
    expect(init_login_page.error_login_message).to_contain_text("Invalid email id and password")  # check the error message

def test_tc06_password_masked(init_login_page):
    """

    :param init_login_page:
    :return:

    Steps:
      1.Type any value into the password field

    Expected: The characters are obscured (input type="password").
    """
    init_login_page.input_password.fill("password")
    expect(init_login_page.input_password).to_have_attribute("type","password")

def test_tc07_forgot_password_nav(init_login_page):
    """

    :param init_login_page:
    :return:

    Steps:
      1. Click the "Forgot password?" link

    Expected: The browser navigates to /forget-password.
    """
    init_login_page.forgot_password()
    expect(init_login_page.page).to_have_url("/forget-password")


