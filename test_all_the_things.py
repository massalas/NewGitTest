from selenium import webdriver
from locators import MainPageLocators
import unittest, Page, time


class TestAllTheThings(unittest.TestCase):
    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test case Test All The Things is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)



    def test_all_the_things(self):


        self.main_page.open_page_and_assert_title(MainPageLocators.BIG_BASKET, "Test All The Things! by ShapewaysCodeTest on Shapeways")
        self.main_page.tab_back()

        self.main_page.open_page_and_assert_title(MainPageLocators.TEST_ALL_THE_THINGS, "Test All The Things! by ShapewaysCodeTest on Shapeways")
        self.main_page.tab_back()

        self.main_page.open_page_and_assert_title(MainPageLocators.CODETEST, "ShapewaysCodeTest on Shapeways")
        self.main_page.tab_back()

        self.main_page.open_page_and_assert_title(MainPageLocators.VISIT_SHOP, "Test All The Things! by ShapewaysCodeTest on Shapeways")
        self.main_page.tab_back()





    def tearDown(self):
        self.main_page.logout()
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()













