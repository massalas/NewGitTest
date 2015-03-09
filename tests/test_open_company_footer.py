import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class CompanyFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Company Footer Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)



    def test_open_company_footer(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.ABOUT_US_FOOTER, "About Us - Shapeways 3D Printing - Shapeways",
        OtherPageLocators.ABOUT_TAG, "About Us")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.BLOG_LINK, "Shapeways Blog - 3D Printing News and Innovation",
        OtherPageLocators.BLOG_TAG, "The Shapeways Blog")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.PRESS_FOOTER, "Press Corner - Shapeways 3D Printing - Shapeways",
        OtherPageLocators.HOW_TAG, "Press Corner")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.CAREERS_FOOTER, "Careers at Shapeways",
        OtherPageLocators.CAREERS_CONTAINER, "Careers at Shapeways")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.BECOME_PARTNER, "Global Partner Network - access to 3D printing around the world through Shapeways - Shapeways",
        OtherPageLocators.PARTNER_TAG, "Shapeways Global Partner Network")


    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()