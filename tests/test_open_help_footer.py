import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class HelpFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Help Footer Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.driver.set_page_load_timeout(30)
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)

    def test_open_help_footer(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.HELP_CENTER_FOOTER, "How can we help? - Shapeways",
        OtherPageLocators.HELP_CONTAINER, "How can we help?")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.CONTACT_US_FOOTER, "Contact Us - Shapeways",
        OtherPageLocators.CONTACT_US_TAG, "Need help with your order or a specific problem?")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.FAQ_FOOTER, "Frequently Asked Questions - Shapeways",
        OtherPageLocators.FAQ_CONTAINER, "Frequently Asked Questions")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.SHIPPING_INFO_FOOTER, "Shipping Information - Shapeways",
        OtherPageLocators.SHIPPING_CONTAINER, "Shipping Information")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.MATERIAL_STATUS, "Materials Shipping Status Page - Shapeways",
        OtherPageLocators.MATERIAL_STATUS_TAG, "Materials Status Page")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.TUTORIALS_FOOTER, "3D Printing & Design Tutorials - Shapeways",
        OtherPageLocators.TUTORIAL_CONTAINER, "3D Printing & Design Tutorials.")



    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()