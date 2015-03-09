import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time


class DesingFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Design Footer Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"



    def test_open_design_footer(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.GETTING_STARTED, "How Shapeways 3D Printing Works",
        OtherPageLocators.GETTING_STARTED_ANCHOR, "How Shapeways 3D Printing Works")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.MATERIALS_FOOTER, "3D Printing Materials: Plastic, Metal, Ceramics and More - Shapeways",
        OtherPageLocators.MATERIALS_ANCHOR, "Plated, Polished, Perfection")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.HIRE_DESIGNER, "Hire a Designer - Shapeways",
        OtherPageLocators.HIRE_DESIGNER_ANCHOR, "Designers for Hire")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.RAPID_PROTO, "Rapid Prototyping & Custom Manufacturing - Shapeways",
        OtherPageLocators.RAPID_ANCHOR, "Rapid prototyping in SLS, metal, and more 3D printing in as few as two days")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.CREATOR_APPS, "Easy 3D Printing Creator Apps",
        OtherPageLocators.CREATOR_ANCHOR, "Easy 3D Printing Apps")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.MAKER_TUTORIALS, "3D Printing & Design Tutorials - Shapeways",
        OtherPageLocators.MAKER_TUTORIAL_ANCHOR, "3D Printing & Design Tutorials.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()