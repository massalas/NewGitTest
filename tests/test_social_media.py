import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time


class SocialMedia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test case Test Social Media is running!"
        print "*" * 10
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)

    def test_social_media(self):
        self.main_page.open_window_assert_title(MainPageLocators.FACEBOOK_ICON, "Facebook")

        self.main_page.open_window_assert_title(MainPageLocators.TWITTER_ICON, "Share a link on Twitter")

        self.main_page.open_window_assert_title(MainPageLocators.PINTEREST_ICON, "Pinterest")


    def tearDown(self):
        self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

