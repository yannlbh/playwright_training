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
    :param init_login_page: pytestfixture to open login page
    :return: null

    """
    init_login_page.login(VALID_EMAIL, VALID_PASSWORD) #login with the good credentials
    expect(init_login_page.success_login_message).to_be_visible() #check the success message
