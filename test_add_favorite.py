import unittest
from selenium import webdriver
from locators import OtherPageLocators
import Page, time

class AddFavorite(unittest.TestCase):

    def setUp(self):
        self.main_page = Page.MainPage(webdriver.Firefox())
        assert self.main_page.is_title_matches(), "Shapeways title doesn't match"
        self.main_page.click_sign_in_link()
        self.main_page.login()
        time.sleep(5)

        """Selects the product and records the favorite status."""
    def test_a_favorite_status(self):
        print "Test case Add Favorite is running!"
        print "Getting the status of the product."
        self.main_page.select_black_product()
        self.main_page.fav_status_before_addition()


        """Add the black product to favorites and also get's its status for verifications."""
    def test_b_add_black_favorite(self):
        print "Adding black favorite and verifying that text has been updated."
        self.main_page.select_white_product()
        self.main_page.select_black_product()
        self.main_page.add_favorite()
        time.sleep(3)
        self.main_page.fav_status_after_addition()
        self.main_page.favorited_text_assertion()

        """Verifies that the product has been added to favorites and the the text
         has changed to "Favorited"."""
    def test_c_favorite_verifications(self):
        print "Verification that fields have been updated properly."
        self.main_page.select_black_product()
        time.sleep(3)
        self.main_page.verification_of_favorite_addition()
        self.main_page.verification_of_favorite_total()



        """Add the white product to favorites and also get's its status for verifications."""
    def test_d_add_white_favorite(self):
        print "Adding white favorite and verifying that text has been updated."
        self.main_page.select_white_product()
        self.main_page.add_favorite()
        time.sleep(3)
        self.main_page.fav_status_after_addition()
        self.main_page.favorited_text_assertion()


        """Goes to the Favorites & Wishlist page and removes the product from the favorites."""
    def test_e_remove_favorite(self):
        print "Removing favorite"
        self.main_page.go_to_favorites_wishlist()
        self.main_page.favorite_remove(OtherPageLocators.WHITE_DESCRIPTION, OtherPageLocators.BLACK_DESCRIPTION)



    def tearDown(self):
        self.main_page.logout()
        self.main_page.close_browser()


if __name__ == "__main__":
    unittest.main()