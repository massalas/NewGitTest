from selenium import webdriver
import unittest, time, Page
from locators import MainPageLocators, OtherPageLocators


class SocialMedia(unittest.TestCase):
    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test case Test Social Media is running!"
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
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()

