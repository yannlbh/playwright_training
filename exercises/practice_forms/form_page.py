from playwright.sync_api import Page

class FormPage(Page):
    def __init__(self, page: Page):
        self.page = page

        # region Form values
        self.country_form = page.get_by_test_id("forms-country")
        self.title_form = page.get_by_test_id("forms-title")
        self.first_name = page.get_by_test_id("forms-first-name")
        self.last_name = page.get_by_test_id("forms-last-name")
        self.date_of_birth = page.get_by_test_id("forms-dob")
        self.date_of_joining = page.get_by_test_id("forms-doj")
        self.email = page.get_by_test_id("forms-email")
        self.phone_code_form = page.get_by_test_id("forms-phone-code")
        self.phone_number = page.get_by_test_id("forms-phone-number")
        #endregion

        # region Button / Checkboxes
        self.pref_comm_method_email = page.get_by_test_id("forms-comm-email")
        self.pref_comm_method_phone = page.get_by_test_id("forms-comm-phone")
        self.clear_button = page.get_by_test_id("forms-clear")
        self.submit_button = page.get_by_test_id("forms-submit")
        #endregion

        # region errors / success messages
        self.success_submit_message = page.get_by_test_id("forms-success")
        self.errors_messages_list = page.locator("small.text-danger")
        #endregion


    def open_form_page(self):
        self.page.goto("/practice-forms")

    def fill_form(self, country_form:str="", title_form:str="", first_name:str="", last_name:str="", date_of_birth:str="", date_of_joining:str="", email:str="", phone_code_form:str="", phone_number:str="", pref_comm_method_email:bool=False, pref_comm_method_phone:bool=False):
        if country_form != "" :
            self.country_form.select_option(country_form)
        if title_form != "" :
            self.title_form.select_option(title_form)
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.date_of_birth.fill(date_of_birth)
        self.date_of_joining.fill(date_of_joining)
        self.email.fill(email)
        if phone_code_form != "" :
            self.phone_code_form.select_option(phone_code_form)
        self.phone_number.fill(phone_number)
        if pref_comm_method_email :
            self.pref_comm_method_email.check()
        if pref_comm_method_phone :
            self.pref_comm_method_phone.check()

    def submit(self):
        self.submit_button.click()

    def clear(self):
        self.clear_button.click()

    def get_error_message_locator(self,message:str):
        return self.errors_messages_list.filter(has_text=message)
