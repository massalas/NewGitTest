import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class TopLeftPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Top Left Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)


    def test_open_top_left_pages(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.SHOP_ICON, "Gift Guide - Shapeways",
        OtherPageLocators.SHOP_ANCHOR, "Shapeways Gift Guide")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.DESIGN_ICON, "Upload your 3D Designs to 3D Print - Shapeways",
        OtherPageLocators.DESIGN_ANCHOR, "3D Printing Made Easy")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.SELL_ICON, "Run Your Business with Shapeways 3D Printing - Shapeways",
        OtherPageLocators.SELL_ANCHOR, "Opening Your Shop")


    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()














