import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class BottomPages(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open Top Pages is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)



    def test_open_top_pages(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.GADGETS_ICON, "Buy Custom Gadgets - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.ACCESSORIES_TOP_ICON, "Buy Custom 3D Printed Accessories - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.JEWELRY_ICON, "Buy Custom Jewelry - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.ART_TOP_ICON, "Buy Custom 3D Printed Art - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.HOME_TOP_ICON, "Buy Custom Products for the Home - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.GAMES_TOP_ICON, "Buy Custom Games & Accessories - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.MINIATURES_ICON, "Buy Custom Miniatures - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.BETA_TOP_ICON, "Beta Products - 3D Printing by Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.MY_LITTLE_PONY_ICON, "My Little Pony by Super Fans for SuperFanArt - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.GIFT_TOP_ICON, "Gift Guide - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.APPS_TOP_ICON, "Easy 3D Printing Creator Apps")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.FEED_TOP_ICON, "Shapeways - 3D Printing Service and Marketplace")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.BLOG_TOP_ICON, "Shapeways Blog - 3D Printing News and Innovation")
        self.main_page.tab_back()




    def tearDown(self):
        self.main_page.logout()


if __name__ == "__main__":
    unittest.main()