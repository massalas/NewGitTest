import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time


class SellFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Sell Footer Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"



    def test_open_sell_footer(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.OPEN_SHOP, "Run Your Business with Shapeways 3D Printing - Shapeways",
        OtherPageLocators.OPEN_SHOP_ANCHOR, "Start selling today")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.DEVELOPER_API, "Make Apps with the Shapeways 3D Printing API",
        OtherPageLocators.DEVELOPER_API_ANCHOR, "Welcome to the Shapeways 3D Printing API")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.SHOPS_TIPS, "Running Your Shop Tutorials - Shapeways",
        OtherPageLocators.SHOP_TIPS_ANCHOR, "Running Your Shop 3D Printing Tutorials")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.OFFER_DESING, "Designer for Hire Submission",
        OtherPageLocators.OFFER_DESIGN_ANCHOR, "Designer for Hire Submission")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()