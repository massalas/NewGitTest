import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time


class AddList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Add List is running!"
        print "*" * 10
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_add_list(self):
        self.main_page.add_list()
        self.main_page.go_to_favorites_wishlist()
        self.main_page.verification_of_list()
        self.main_page.delete_list()


    def tearDown(self):
        self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()