import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class SocialFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Social Footer Pages is running!"
        print "*" * 10
        #self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)


    def test_open_social_footer(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.FACEBOOK_FOOTER, "Shapeways | Facebook",
        OtherPageLocators.FB_ELEMENT, "To connect with Shapeways, sign up for Facebook today.")
        self.driver.back()
        print "next test"


        self.main_page.open_page_and_assert_title(MainPageLocators.TWITTER_FOOTER, "Shapeways (@shapeways) | Twitter",
        OtherPageLocators.TWITTER_HEADER, "Shapeways")
        self.driver.back()
        print "next test"


        self.main_page.open_page_and_assert_title(MainPageLocators.INSTAGRAM_FOOTER, "shapeways (@shapeways) ? Instagram photos and videos",
        OtherPageLocators.INSTAGRAM_TAG, "Instagram")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.YOUTUBE_FOOTER, "  Shapeways - YouTube",
        OtherPageLocators.UTUBE_ELEMENT, "What to Watch")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.MEETUP_FOOTER, "Shapeways (New York, NY) - Meetup",
        OtherPageLocators.MEETUP_LOCALITY, "New York")
        self.driver.back()
        print "next test"


        self.main_page.open_page_and_assert_title(MainPageLocators.TUMBLR_FOOTER, "Shapeways 3D Printspiration",
        OtherPageLocators.TUMBLR_ELEMENT, "FOLLOW ON TUMBLR")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.FLICKR_FOOTER, "Flickr: Shapeways:'s Photostream",
        OtherPageLocators.FLICKR_ANCHOR, "Photostream")
        self.driver.back()
        print "next test"




    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


















