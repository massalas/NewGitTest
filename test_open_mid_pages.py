import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class Add_Favorite(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open Mid Pages is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)



    def test_open_bottom_pages(self):



        self.main_page.open_page_and_assert_title(MainPageLocators.ART_ICON, "Buy Custom 3D Printed Art - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.ACCESSORIES1_ICON, "Buy Custom Accessories for the Home - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.SCULPTURES_ICON, "Buy Custom Sculptures - Shapeways 3D Printing")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.ACCESSORIES2_ICON, "Shapeways | Search Results")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.BEER_ICON, "Shapeways | Search Results")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.GRUMPY_ICON, "Shapeways | Search Results")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.HOME_ICON, "Shapeways | Search Results")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.HOMEBREW_ICON, "Shapeways | Search Results")
        self.main_page.tab_back()




    def tearDown(self):
        self.main_page.logout()
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()