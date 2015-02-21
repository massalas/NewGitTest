import unittest
from selenium import webdriver
from locators import MainPageLocators
import Page, time

class LegalFooter(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Open Legal Footer Pages is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)





    def test_open_legal_footer(self):
        self.main_page.open_page_and_assert_title(MainPageLocators.PRIVACY_FOOTER, "Shapeways | privacy statement")
        self.main_page.tab_back
        self.main_page.open_page_and_assert_title(MainPageLocators.TERMS_FOOTER, "Shapeways | terms & conditions")
        self.main_page.tab_back
        self.main_page.open_page_and_assert_title(MainPageLocators.POLICY_FOOTER, "Shapeways | content policy")
        self.main_page.tab_back




    def tearDown(self):
        self.main_page.logout()


if __name__ == "__main__":
    unittest.main()


















