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
        print "Test Open Top Pages is running!"
        print "*" * 10
        #self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.driver.set_page_load_timeout(30)
        #.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)

    def test_open_top_pages(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.GADGETS_ICON, "Buy Custom Gadgets - Shapeways 3D Printing",
         OtherPageLocators.TAG, "Gadgets")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.ACCESSORIES_TOP_ICON, "Buy Custom 3D Printed Accessories - Shapeways 3D Printing",
        OtherPageLocators.TAG, "Accessories")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.JEWELRY_ICON, "Buy Custom Jewelry - Shapeways 3D Printing",
        OtherPageLocators.TAG, "Jewelry")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.ART_TOP_ICON, "Buy Custom 3D Printed Art - Shapeways 3D Printing",
        OtherPageLocators.TAG, "Art")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.HOME_TOP_ICON, "Buy Custom Products for the Home - Shapeways 3D Printing",
        OtherPageLocators.TAG, "For Your Home")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.GAMES_TOP_ICON, "Buy Custom Games & Accessories - Shapeways 3D Printing",
        OtherPageLocators.TAG, "Games")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.MINIATURES_ICON, "Buy Custom Miniatures - Shapeways 3D Printing",
        OtherPageLocators.TAG, "Miniatures")



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()