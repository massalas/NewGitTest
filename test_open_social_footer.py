import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class SocialFooter(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open Social Footer Pages is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_open_social_footer(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.TWITTER_FOOTER, "Shapeways (@shapeways) | Twitter")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.FLICKR_FOOTER, "Flickr: Shapeways:'s Photostream")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.MEETUP_FOOTER, "Shapeways (New York, NY) - Meetup")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.FACEBOOK_FOOTER, "Shapeways | Facebook")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.TUMBLR_FOOTER, "Shapeways 3D Printspiration")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.YOUTUBE_FOOTER, "  Shapeways - YouTube")
        self.main_page.tab_back()



    def tearDown(self):
        self.main_page.logout()


if __name__ == "__main__":
    unittest.main()


















