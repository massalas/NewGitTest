import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class BottomPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Top Pages Part2 is running!"
        print "*" * 10
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_open_top_pages(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.BETA_TOP_ICON, "Beta Products - 3D Printing by Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.MY_LITTLE_PONY_ICON, "My Little Pony by Super Fans for SuperFanArt - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.GIFT_TOP_ICON, "Gift Guide - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.APPS_TOP_ICON, "Easy 3D Printing Creator Apps")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.FEED_TOP_ICON, "Shapeways - 3D Printing Service and Marketplace")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.BLOG_TOP_ICON, "Shapeways Blog - 3D Printing News and Innovation")
        self.main_page.tab_back()


    def tearDown(self):
        self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()