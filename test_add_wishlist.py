from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import Page, time, unittest


class WishList(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        print "Test case Wishlist is running!"
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(3)


    def test_wishlist(self):
        self.main_page.add_wishlist()
        self.main_page.wishlist_verification()
        self.main_page.go_to_favorites_wishlist()
        self.main_page.wishlist_page_verification()
        self.main_page.remove_wishlist()


    def tearDown(self):
        self.main_page.logout()

if __name__ == "__main__":
    unittest.main()
