import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libs.generators import Generators


class BasePage:

    # Тут описываются локаторы
    LOGOUT_BUTTON = ("xpath", "//button[@id='logout']")
    LOGO_LINK = ("xpath", "//a[@id='logo']")
    ...

    # Тут создаются необходимые обьекты, которые будут доступны в pages
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.generators = Generators()

    # Данный метод будет вызываться для любой страницы, принимая ее PAGE_URL
    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"): # "этот метод явл тестовым шагом, поэтому маркируем его аллюром
            self.driver.get(self.PAGE_URL)

    # Ниже описываются общие для всех страниц методы
    def find(self, lokator):                             # "эти методы не явл тестовым шагом, поэтому не маркируем их аллюром:
        return self.driver.find_element("xpath", locator)

    # метод, который ждет, пока элемент найдется,
    # return -
    #делает так, что этот метод возвзащает найденный элемент и тогда
    #уже в login_page можно кликать на этот вызванный элемент или
    # делать что-то еще с ним
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located("xpath", locator))

        # def click_on_logout_button(self):
        #     self.driver.find_element(*self.LOGOUT_BUTTON).click()