import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = "https://demoqa.com/login"

    USERNAME_FIELD = "//input[@id='userName']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_BUTTON = "//button[@id='login']"

    @allure.step("Enter username")
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)