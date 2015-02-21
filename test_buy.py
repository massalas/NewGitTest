import unittest
from selenium import webdriver
import Page, time

class Buy_item(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Buy is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_buy_item(self):
        self.main_page.buy()



    def tearDown(self):
        self.main_page.logout()

if __name__ == "__main__":
    unittest.main()