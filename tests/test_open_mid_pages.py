import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class Add_Favorite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Mid Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        #self.driver.set_page_load_timeout(30)
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)

    def test_open_mid_pages(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.ART_ICON, "Buy Custom 3D Printed Art - Shapeways 3D Printing",
        OtherPageLocators.ART_TAG, "Art")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.ACCESSORIES1_ICON, "Buy Custom Accessories for the Home - Shapeways 3D Printing",
         OtherPageLocators.ACCESSORIES_CONTAINER, "For Your Home")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.SCULPTURES_ICON, "Buy Custom Sculptures - Shapeways 3D Printing",
        OtherPageLocators.SCULPTURES_CONTAINER, "Sculptures")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.ACCESSORIES2_ICON, "Shapeways | Search Results",
        OtherPageLocators.TAG_ACCESSORIES, "Tag: accessories")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.BEER_ICON, "Shapeways | Search Results",
        OtherPageLocators.BEER_TAG, "Tag: Beer")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.GRUMPY_ICON, "Shapeways | Search Results",
        OtherPageLocators.GRUMPY_TAG, "Tag: Grumpy")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.HOME_ICON, "Shapeways | Search Results",
        OtherPageLocators.HOME_TAG, "Tag: home")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.HOMEBREW_ICON, "Shapeways | Search Results",
        OtherPageLocators.HOMEBREW_TAG, "Tag: Homebrew")


    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()