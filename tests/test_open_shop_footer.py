import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class ShopFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Shop Footer Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)



    def test_open_shop_footer(self):


        self.main_page.open_page_and_assert_title(MainPageLocators.MARKET_PLACE, "Gift Guide - Shapeways",
         OtherPageLocators.MARKETPLACE_ANCHOR, "Shapeways Gift Guide" )
        self.driver.back()
        print "next test"


        self.main_page.open_page_and_assert_title(MainPageLocators.GIFT_GUIDE, "Gift Guide - Shapeways",
         OtherPageLocators.GIFT_GUIDE_ANCHOR, "Shapeways Gift Guide" )
        self.driver.back()
        print "next test"


        self.main_page.open_page_and_assert_title(MainPageLocators.BETA_PRODUCTS, "Beta Products - 3D Printing by Shapeways",
         OtherPageLocators.BETA_PAGE_ANCHOR, "Beta Products" )
        self.driver.back()
        print "next test"


        self.main_page.open_page_and_assert_title(MainPageLocators.GIFT_CARDS, "Shapeways Gift Cards",
         OtherPageLocators.GIFT_CARDS_ANCHOR, "Shapeways Gift Cards" )
        self.driver.back()
        print "next test"



    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()