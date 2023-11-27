import allure
import pytest
from pages.login_page import LoginPage


import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


#@pytest.mark.usefixtures("driver")  # Фикстура драйвера
class TestLoginPage:

    def setup(self):
        self.login_page = LoginPage(self.driver)  # Создаем обьект страницы

    # Вызываем через объект страницы все нужные методы, это и есть шаги теста
    @allure.title("Example")
    def test_login_in_account(self):
        self.login_page.open()  # open() подхватит PAGE_URL именно с LoginPage
        self.login_page.enter_username()
        self.login_page.enter_password()
        self.login_page.click_on_login_button()