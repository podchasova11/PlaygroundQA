import allure
from config.base_page import BasePage
from data.links import Links


class ContactPage(BasePage):

    PAGE_URL = Links.CONTACT_PAGE
    NEW_CONTACT_BUTTON = "//a[@aria-label='New Contact']"

    # USERNAME_FIELD = "//input[@id='userName']"
    # PASSWORD_FIELD = "//input[@id='password']"
    # LOGIN_BUTTON = "//button[@id='login']"
    @allure.step("Click on new contact button")
    def click_on_new_contact_button(self):
        self.find(self.NEW_CONTACT_BUTTON).click()

    @allure.step("Enter username")
    def enter_username(self):
        # with allure .step(f"Enter username {username}"):
        self.find(self.USERNAME_FIELD).send_keys(self.generators.generate_email(10))

    # def enter_login(self):
    #     pass
    @allure.step("Enter password")
    def enter_password(self):
        self.find(self.PASSWORD_FIELD).send_keys(self.generators.generate_password(6))
        self.wait_for_visibility(self.PASSWORD_FIELD).click()

    @allure.step("Click on login button")
    def click_on_login_button(self):
        self.find(self.LOGOUT_BUTTON).click()

