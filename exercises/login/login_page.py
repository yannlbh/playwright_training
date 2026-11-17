from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page #web page
        self.input_email = page.get_by_test_id("login-email") #input for email login
        self.input_password = page.get_by_test_id("login-password") #input for password login
        self.button_login = page.get_by_test_id("login-submit") #button to submit login
        self.success_login_message = page.get_by_test_id("login-success") #message when success login
        self.error_login_message = page.get_by_test_id("login-error") #error message for wrong credentials
        self.button_forgot_password = page.get_by_test_id("login-forgot-password")

    def open_login_page(self):
        self.page.goto("/practice-login-form") #direct the page to login form

    def login(self, email:str, password:str):
        if email :
            self.input_email.fill(email) #fill the email input
        if password :
            self.input_password.fill(password) #fill the password input
        self.button_login.click() #try to login

    def forgot_password(self):
        self.button_forgot_password.click()