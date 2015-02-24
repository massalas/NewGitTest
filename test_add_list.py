from selenium import webdriver
import Page, time, unittest
from locators import OtherPageLocators, MainPageLocators


class AddList(unittest.TestCase):
    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Add List is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_add_list(self):
        self.main_page.add_list()
        self.main_page.go_to_favorites_wishlist()
        self.main_page.verification_of_list()
        self.main_page.delete_list()



    def tearDown(self):
        self.main_page.logout()
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()