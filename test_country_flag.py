import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class CountryFlag(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
       	self.main_page.delete_cookies()
        print "Test Flag is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"


    def test_a_country_selection(self):
        self.main_page.get_cost()
        self.main_page.move_mouse_to_element_and_click(MainPageLocators.COUNTRY_FLAG)
        self.main_page.change_currency_to_country("Greece")
        #self.main_page.encode(MainPageLocators.CURRENCY_SYMBOL_ID)

        self.main_page.verify_currency_changed()







if __name__ == "__main__":
    unittest.main()