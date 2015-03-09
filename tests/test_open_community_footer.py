import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time


class CommunityFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Community Footer Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"



    def test_open_community_footer(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.FORUMS_FOOTER, "Shapeways 3D Printing Forums",
        OtherPageLocators.FORUM_ANCHOR, "Shapeways")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.EVENTS_FOOTER, "Shapeways | Events",
        OtherPageLocators.EVENTS_ANCHOR, "Community Events and Meetups")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.JOIN_CREW, "Join the World's Largest 3D Printing Community - Shapeways",
        OtherPageLocators.JOIN_CREW_ANCHOR, "Shapeways 3D Printing Community")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.EDUCATION_FOOTER, "Shapeways Education Program",
        OtherPageLocators.EDUCATION_ANCHOR, "Sign up for Shapeways Education Program to save on your 3D prints and be a part of the world's largest 3D printing community")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()