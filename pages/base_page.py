
class BasePage:

    # Тут описываются локаторы
    LOGOUT_BUTTON = ("xpath", "//button[@id='logout']")
    LOGO_LINK = ("xpath", "//a[@id='logo']")
    ...

    # Тут создаются необходимые обьекты, которые будут доступны в pages
    def __init__(self, driver):
        self.driver = driver
        ...

    # Данный метод будет вызываться для любой страницы, принимая ее PAGE_URL
    def open(self):
        self.driver.get(self.PAGE_URL)

    # Ниже описываются общие для всех страниц методы
    def click_on_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()