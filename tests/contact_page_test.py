import time

import allure
from pip._vendor import requests

from config.base_test import BaseTest
# from pages.contact_card_page import ContactCardPage
# from pages.contact_page import ContactPage
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options


@allure.feature("Contacts")
class TestContacts(BaseTest):

    @allure.title("Add new contact")
    def test_add_new_contact(self):
        self.contact_page.open()
        self.contact_page.click_on_new_contact_button()
        self.contact_card_page.enter_first_name("Mila")
        self.contact_card_page.enter_last_name("Podchasova")
        self.contact_card_page.enter_title_field("Hgsxg")
        self.contact_card_page.enter_email("mmmmmmila@ya.ru")
        self.contact_card_page.click_on_submit_button()
        self.contact_card_page.enter_email(self.generators.generate_email(10))
        self.contact_card_page.click_on_submit_button()
        time.sleep(5)


    # @pytest.mark.usefixtures("get_driver")
    # @allure.title("Example")
    # def test_login_in_account(self):
    #     self.driver.get("https://demoqa.com/login")
        # self.login_page.open()  # open() подхватит PAGE_URL именно с LoginPage
        # self.login_page.enter_username()
        # self.login_page.enter_password()
        # self.login_page.click_on_login_button()

    # def setup(self, get_driver):
    #     self.login_page = LoginPage.PAGE_URL(self, get_driver) # Создаем обьект страницы
    # # Вызываем через объект страницы все нужные методы, это и есть шаги теста