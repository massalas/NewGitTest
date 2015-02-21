import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class HelpFooter(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open Help Footer Pages is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)

    def test_open_help_footer(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.HELP_CENTER_FOOTER, "How can we help? - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.CONTACT_SUPPORT_FOOTER, "Contact Us - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.FAQ_FOOTER, "Frequently Asked Questions - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.SHIPPING_INFO_FOOTER, "Shipping Information - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.TUTORIALS_FOOTER, "3D Printing & Design Tutorials - Shapeways")
        self.main_page.tab_back()


    def tearDown(self):
        self.main_page.logout()


if __name__ == "__main__":
    unittest.main()