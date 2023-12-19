#import time
#import sqlite3
import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True, scope="class")
def get_driver(request):
    # service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

# # Установка соединения с базой данных
# def connect_database():
#     connection = sqlite3.connect('test.db')
#     print("Соединение с БД установлено")
#
# # Возвращение соединения с БД
#     return connection
#
