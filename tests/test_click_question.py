import sys
sys.path.append("../")
sys.path.append("../../")
from objects import Page
from config.locators import MainPageLocators, OtherPageLocators
import unittest
from selenium import webdriver
import time


class ClickQuestion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = Page.MainPage(self.driver)
        print "Test Click Question is running!"
        print "*" * 10
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_click_question(self):
        self.main_page.move_mouse_to_element_and_click(MainPageLocators.QUESTIONMARK)
        self.main_page.open_window_assert_title(MainPageLocators.LEARN_MORE, "Developing Your Product at Shapeways - Shapeways")



    def tearDown(self):
        self.main_page.logout()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


