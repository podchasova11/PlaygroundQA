from libs.generators import Generators
from pages.contact_page import ContactPage
from pages.contact_card_page import ContactCardPage


class BaseTest:

    def setup(self):
        # Pages
        self.contact_page = ContactPage(self.driver)
        self.contact_card_page = ContactCardPage(self.driver)

        # Libs
        self.generators = Generators
