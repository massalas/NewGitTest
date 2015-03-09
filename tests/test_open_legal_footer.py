import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time

class LegalFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Open Legal Footer Pages is running!"
        print "*" * 10
        self.driver.delete_all_cookies()
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        #self.main_page.click_sign_in_link()
        #self.main_page.login()
        #time.sleep(3)


    def test_open_legal_footer(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.PRIVACY_FOOTER, "Shapeways | privacy statement",
        OtherPageLocators.PRIVACY_CONTAINER, "Shapeways Privacy Statement")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.TERMS_FOOTER, "Shapeways | terms & conditions",
        OtherPageLocators.TERMS_CONTAINER, "Shapeways Terms and Conditions")
        self.driver.back()
        print "next test"

        self.main_page.open_page_and_assert_title(MainPageLocators.POLICY_FOOTER, "Shapeways | content policy",
        OtherPageLocators.CONTENT_POLICY_CONTAINER, "Shapeways Content Policy and Notice Takedown Procedure")


    def tearDown(self):
        #self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


















