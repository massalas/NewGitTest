import unittest
from selenium import webdriver
from locators import MainPageLocators, OtherPageLocators
import Page, time

class Dropdown(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open DropDown Options is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)





    def test_dropdown_options(self):

        self.main_page.drop_down(MainPageLocators.NOTIFICATIONS_DROPDOWN, "Shapeways - 3D Printing Service and Marketplace",
        OtherPageLocators.NOTIFICATIONS_TAG, "Notifications")
        self.main_page.tab_back()

        self.main_page.drop_down(MainPageLocators.MYFEED_DROPDOWN, "Shapeways - 3D Printing Service and Marketplace",
        OtherPageLocators.MYFEED_TAG, "My Feed")
        self.main_page.tab_back()


        self.main_page.drop_down(MainPageLocators.ORDERS_DROPDOWN, "Shapeways - 3D Printing Service and Marketplace",
        OtherPageLocators.ORDERS_TAG, "My Orders")
        self.main_page.tab_back()


        self.main_page.drop_down(MainPageLocators.MODELS_DROPDOWN, "My Models - Shapeways", OtherPageLocators.MODELS_TAG, "My Models")
        self.main_page.tab_back()

        self.main_page.drop_down(MainPageLocators.PROFILE_DROPDOWN, "mxll on Shapeways", OtherPageLocators.PROFILE_TAG, "mxll")
        self.main_page.tab_back()


        self.main_page.drop_down(MainPageLocators.FAV_N_WISHLIST, "Shapeways - 3D Printing Service and Marketplace",
        OtherPageLocators.FAV_N_WISH_TAG, "Favorites")
        self.main_page.tab_back()


        self.main_page.drop_down(MainPageLocators.SETTINGS_DROPDOWN, "Shapeways - 3D Printing Service and Marketplace",
        OtherPageLocators.SETTINGS_TAG, "Email Address")
        self.main_page.tab_back()




    def tearDown(self):
        self.main_page.logout()
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()