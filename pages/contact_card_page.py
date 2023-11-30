import allure

from pages.base_page import BasePage
from data.links import Links


class ContactCardPage(BasePage):

    PAGE_URL = Links.CONTACT_PAGE

    FIRST_NAME_FIELD = "//input[@id='first_name']"
    LAST_NAME_FIELD = "//input[@id='last_name']"
    TITLE_FIELD = "//input[@id='title']"
    EMAIL_FIELD = "//input[@id='email']"
    SUBMIT_BUTTON = "//button[@type='submit']"

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        self.find(self.FIRST_NAME_FIELD).send_keys(first_name)

    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        self.find(self.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step("Enter title field")
    def enter_title_field(self, title_field):
        self.find(self.TITLE_FIELD).send_keys(title_field)

    @allure.step("Enter email")
    def enter_email(self, email):
        self.find(self.EMAIL_FIELD).send_keys(email)

    @allure.step("Click on submit button")
    def click_on_submit_button(self):
        self.find(self.SUBMIT_BUTTON).click()
