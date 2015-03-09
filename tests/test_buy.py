import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class Buy_item(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Buy is running!"
        print "*" * 10
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_buy_item(self):
        self.main_page.check_cart_is_present()
        for i in xrange(10):
            self.main_page.buy()
            self.main_page.check_cart_is_present()
        self.main_page.click_element(MainPageLocators.CART_ICON)
        self.main_page.assert_page_has_been_accessed(OtherPageLocators.YOUR_CART_ANCHOR, "Your Cart")
        self.main_page.assert_title_matches("Shopping Cart - Shapeways")
        self.main_page.click_element(OtherPageLocators.REMOVE_ITEM)
        self.driver.back()



    def tearDown(self):
        self.main_page.logout()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()