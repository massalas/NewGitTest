import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time


class TestAllTheThings(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test case Test All The Things is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)



    def test_all_the_things(self):


        self.main_page.open_page_and_assert_title(MainPageLocators.BIG_BASKET, "Test All The Things! by ShapewaysCodeTest on Shapeways",
        OtherPageLocators.TEST_ALL_TAG, "Test All The Things!" )
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.TEST_ALL_THE_THINGS, "Test All The Things! by ShapewaysCodeTest on Shapeways",
        OtherPageLocators.TEST_ALL_TAG, "Test All The Things!")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.CODETEST, "ShapewaysCodeTest on Shapeways",
        OtherPageLocators.CODETEST_TAG, "ShapewaysCodeTest")
        self.driver.back()
        print "next test"


        self.main_page.open_page_and_assert_title(MainPageLocators.VISIT_SHOP, "Test All The Things! by ShapewaysCodeTest on Shapeways",
        OtherPageLocators.TEST_ALL_TAG, "Test All The Things!")



    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()













