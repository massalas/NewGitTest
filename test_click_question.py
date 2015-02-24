from selenium import webdriver
import Page, time, unittest
from locators import MainPageLocators


class ClickQuestion(unittest.TestCase):
    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test Click Question is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_click_question(self):
        self.main_page.move_mouse_to_element_and_click(MainPageLocators.QUESTIONMARK)
        self.main_page.open_window_assert_title(MainPageLocators.LEARN_MORE, "Developing Your Product at Shapeways - Shapeways")



    def tearDown(self):
        self.main_page.logout()
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()


