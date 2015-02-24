import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class TopLeftPages(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open Top Left Pages is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)



    def test_open_top_left_pages(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.SHOP_ICON, "Gift Guide - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.DESIGN_ICON, "Upload your 3D Designs to 3D Print - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.SELL_ICON, "Run Your Business with Shapeways 3D Printing - Shapeways")
        self.main_page.tab_back()




    def tearDown(self):
        self.main_page.logout()
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()














