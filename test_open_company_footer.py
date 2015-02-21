import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class CompanyFooter(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open Company Footer Pages is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)



    def test_open_company_footer(self):

        self.main_page.open_page_and_assert_title(MainPageLocators.ABOUT_US_FOOTER, "About Us - Shapeways 3D Printing - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.HOW_WORKS_FOOTER, "How Shapeways 3D Printing Works")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.PRESS_FOOTER, "Press Corner - Shapeways 3D Printing - Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.CONTACT_US_FOOTER, "Shapeways | Contact us")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.CAREERS_FOOTER, "Careers at Shapeways")
        self.main_page.tab_back()
        self.main_page.open_page_and_assert_title(MainPageLocators.DEVELOPERS_FOOTER, "Make Apps with the Shapeways 3D Printing API")





    def tearDown(self):
        self.main_page.logout()


if __name__ == "__main__":
    unittest.main()