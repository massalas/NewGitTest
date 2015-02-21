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



    def tearDown(self):
        self.main_page.logout()


if __name__ == "__main__":
    unittest.main()