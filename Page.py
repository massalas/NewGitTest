from locators import MainPageLocators, OtherPageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal
import time

class MainPage(object):


    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(31)
        self.driver.get("https://www.shapeways.com/product/DM8QHNHJS/taphandle?optionId=7360379")
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True


    #    sauce_url = "http://massalas:28c5a380-a6c3-4ae1-8a19-fcf7abc381d1@ondemand.saucelabs.com:80/wd/hub"
    #   desired_capabilities = {
    #   'platform': "OS X 10.10",
    #   'browserName': "Firefox",
    #   'version': "35.0",
    #   }

    #  self.driver = webdriver.Remote(desired_capabilities=desired_capabilities,
    #                          command_executor=sauce_url)

    #   self.driver.implicitly_wait(5)
    #    self.driver_url = "http://www.shapeways.com/product/DM8QHNHJS/taphandle?"
    #    self.verificationErrors = []
    #    self.accept_next_alert = True
    #    sauce_client = SauceClient("massalas", "28c5a380-a6c3-4ae1-8a19-fcf7abc381d1")

    #   sauce_client.jobs.update_job(self.driver.session_id, passed=True)

        """Destructor!"""
    def __del__(self):
        self.driver.close()

        """ Setup to be used when cross browser testing takes place """
#    def setUp(self):
        # self.driver = webdriver.Firefox()


    def is_title_matches(self):
        return "TapHandle" in self.driver.title

    def tab_back(self):
        self.driver.back()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

        """ Simply clicks at an element using the css selector."""
    def click_element(self, link):
        element = self.driver.find_element_by_css_selector(link)
        element.click()


    """ Simply clicks at an element using id"""
    def click_element_by_id(self, link):
        element = self.driver.find_element_by_id(link)
        element.click()


        """ Simply selects the SignIN link of main page. """
    def click_sign_in_link(self):
        sign_in = self.driver.find_element_by_css_selector(MainPageLocators.SIGN_IN_LINK)
        sign_in.click()


        """ Function LOGIN"""
    def login(self):
        username_mass = "mxll"
        pass_mass = "fornaroli1978van"
        user_name = self.driver.find_element_by_id(MainPageLocators.USER_NAME_FIELD)
        user_name.clear()
        user_name.send_keys(username_mass)
        password = self.driver.find_element_by_id(MainPageLocators.PASSWORD_FIELD)
        password.clear()
        password.send_keys(pass_mass)
        login_button = self.driver.find_element_by_css_selector(MainPageLocators.LOGIN_BUTTON)
        login_button.click()



        """ Function LOGOUT """
    def logout(self):
        element_to_hover_over = self.driver.find_element_by_css_selector(MainPageLocators.DROPDOWN_ARROW)            # Drop down arrow

        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

        try: sign_out = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.SIGN_OUT)).click()          # Sign out element
        except Exception:
            raise



        """ Selects the buy button of the main page and then the checkout icon of the cart pop-up. """
    def buy(self):

        try: buy = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.BUY_BUTTON))          # Buy now button
        except Exception:
            raise

        buy.click()

        try: checkout = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.CHECKOUT_BUTTON))           # Checkout button
        except Exception:
            raise

        checkout.click()


        """ Funtion that selects the favorite icon of the main page."""
    def add_favorite(self):
        try: favorite_icon = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_ICON))
        except Exception:
            raise


        favorite_icon.click()


        """ Selects the wishlist icon"""
    def add_wishlist(self):
        try: wishlist_icon = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.WISH_ICON))
        except Exception:
            raise

        wishlist_icon.click()



        """ Function that verifies that the text has changed to wishlisted."""
    def wishlist_verification(self):
        time.sleep(5)
        try: wishlisted = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.WISHLISTED)).text
        except Exception:
            raise

        try: assert "Wishlisted" in wishlisted
        except Exception:
            raise


        """ Function that verifies product exists in the Wishlisted page tab"""
    def wishlist_page_verification(self):
        try: wish_tab = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_TAB))
        except Exception:
            raise

        wish_tab.click()

        try: wish_image = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_IMAGE))
        except Exception:
            raise




        """ In this function we get the data from the fields Favorite by more and total users
            that have favorited the product in order to use it in the favorite verification functions."""
    def fav_status_before_addition(self):
        global favorites_more, favorites_total
        favorites_m = self.driver.find_element_by_css_selector(MainPageLocators.FAVORITED_MORE).text              # Favorited by more element
        favorites_more = int(favorites_m)
        favorites_t = self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL).text             # Favorites total element
        favorites_total = int(favorites_t)


        """ In the function below we get the data of the favorite more and total users after the favorite icon has been pressed.
            This way we will compare the results based on the data that we got in function "fav_status_before_addition"."""
    def fav_status_after_addition(self):
        global favorites_more_plus, favorites_total_plus
        favorites_m_plus = self.driver.find_element_by_css_selector(MainPageLocators.FAVORITED_MORE).text              # Favorited by more element
        favorites_more_plus = int(favorites_m_plus)
        favorites_t_plus = self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL).text             # Favorites total element
        favorites_total_plus = int(favorites_t_plus)


        """ We verify that the Favorite text field changes to "Favorited" after the favorite icon is pressed."""
    def favorited_text_assertion(self):
        try: elem = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITE_TEXT)).text            # Favorite text
        except Exception:
            raise

        assert "Favorited" in elem
        print "Text verified, value is %s" % elem


        """ Verifies that the favorite more field has been updated correctly by comparing the  data from
            "fav_status_before_addition" and "fav_status_after_addition" functions. """
    def verification_of_favorite_addition(self):
        assert(favorites_more + 1 == favorites_more_plus)
        print "Favorites more equals: %r , favorites_more_plus equals: %r" % (favorites_more, favorites_more_plus)



        """ Verifies that the favorite total field has been updated correctly by comparing the  data from
            "fav_status_before_addition" and "fav_status_after_addition" functions. """
    def verification_of_favorite_total(self):

        assert(favorites_total + 1 == favorites_total_plus)
        print "Favorites total equals: %r , favorites_total_plus equals: %r" % (favorites_total, favorites_total_plus)



        """ Simple function that selects the Favorites & Wishlist option from the drop down menu. """
    def go_to_favorites_wishlist(self):
        self.driver.find_element_by_css_selector(MainPageLocators.DROPDOWN_ARROW).click()           # Drop down arrow element
        self.driver.find_element_by_css_selector(MainPageLocators.FAV_N_WISHLIST).click()       # Favorites & Wishlist element



        """ Removes favorite product from the Favorite & Wishlist page. """
    def favorite_remove(self, white, black):

        if self.is_element_present(By.CSS_SELECTOR, white):
            remove_white = self.driver.find_element_by_css_selector(OtherPageLocators.WHITE_REMOVE).click()
            print "White product has been removed!"
        elif white == "none":
            print "Nothing to remove."
        else:
            return False

        if self.is_element_present(By.CSS_SELECTOR, black):
            remove_black = self.driver.find_element_by_css_selector(OtherPageLocators.BLACK_REMOVE).click()
            print "Black product has been removed!"
        elif black == "none":
            print "Nothing to remove."
        else:
            return False


        #if self.assertTrue(WebDriverWait(self.driver, 10).until(lambda driver : self.is_element_present(By.CSS_SELECTOR, OtherPageLocators.WHITE_DESCRIPTION))):
        #    remove_white = self.driver.find_element_by_css_selector(OtherPageLocators.WHITE_REMOVE).click()
        #elif self.assertTrue(WebDriverWait(self.driver, 10).until(lambda driver : self.is_element_present(By.CSS_SELECTOR, OtherPageLocators.BLACK_DESCRIPTION))):
        #    remove_black = self.driver.find_element_by_css_selector(OtherPageLocators.BLACK_REMOVE).click()
        #else:
        #    return False



        """ Removes wishlisted product from the Favorite & Wishlist page. """
    def remove_wishlist(self):
        try: image = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_IMAGE))          # Wishlist image
        except Exception:
            raise

        try: remove = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.REMOVE_FAVORITE))            # Remove favorite n wishlist button
        except Exception:
            raise

        remove.click()



        """ Selects the white product. """
    def select_white_product(self):
        try: white = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.WHITE_PRODUCT))            # White product little button
        except Exception:
            raise

        white.click()


        """ Selects the black product. """
    def select_black_product(self):
        try: black = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.BLACK_PRODUCT))            # Black product little button
        except Exception:
            raise

        black.click()


        """ Basic function that clicks at a page link and verifies that the page has been loaded by checking the title page. """
    def open_page_and_assert_title(self, element_locator, page_title):
        self.verificationErrors = []

        try: page_icon = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(element_locator))           # Page icon
        except AssertionError as e: self.verificationErrors.append(str(e))


        page_icon.click()
        time.sleep(2)
        try: assert self.driver.title in page_title
        except AssertionError as e: self.verificationErrors.append(str(e))
        print self.driver.title
        time.sleep(3)

        # driver.back()


        """ This function opens the drop down menu at the top right and verifies that the selected option has been loaded"""
    def drop_down(self, element_locator, page_title, tag, tag_name):
        try: element_to_hover_over = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.DROPDOWN_ARROW))           # Drop down arrow
        except Exception:
            raise


        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        element_to_hover_over.click()

        try: drop_option = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(element_locator)).click()         # Drop down element
        except Exception:
            raise


        try: home_tag = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(tag)).text           # Tag locator
        except Exception:
            raise


        if home_tag == tag_name:
            print "Tag verified, tag value is: %s" % home_tag
        else:
            print "Error! is %s" % home_tag

        print self.driver.title
        try: assert self.driver.title in page_title
        except Exception:
            raise


        """ Function below opens the tab and verifies that it has been loaded correctly."""
    def open_tab_and_assert_title(self, element_locator, page_title):
        parent_tab = self.driver.current_window_handle

        try: page_icon = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(element_locator))           # Page icon
        except Exception:
            raise

        page_icon.click()
        time.sleep(3)

        newtab = self.driver.current_window_handle
        try: assert self.driver.title == page_title
        except AssertionError:
            return False


#        except AssertionError as e: self.verificationErrors.append(str(e))
#        print driver.title
        time.sleep(3)
        self.driver.switch_to_window(parent_tab)
        time.sleep(3)


        """ The function below selects the List icon in the main screen and proceeds
         to the creation of a new list"""
    def add_list(self):
        try: list_icon = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.ADD_TO_LIST))
        except Exception:
            raise

        list_icon.click()

        try: list_field = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(OtherPageLocators.ADD_LIST_FIELD))
        except Exception:
            raise

        list_field.send_keys("Test!")

        self.driver.find_element_by_id(OtherPageLocators.CREATE_LIST_BUTTON).click()
        self.driver.find_element_by_id(OtherPageLocators.DONE_LIST_BUTTON_ID).click()


        """ Verifies that list appears in the drop down menu of the Fav & Wishlist page."""
    def verification_of_list(self):
        try: list_drop_down = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(OtherPageLocators.OTHER_LISTS_ID))
        except Exception:
            raise

        list_drop_down.click()

        try: test_list = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.LIST_DROP_DOWN))
        except Exception:
            raise


        """ Deletion of the created list from the manage list menu."""
    def delete_list(self):
        manage_lists = self.driver.find_element_by_id(OtherPageLocators.MANAGE_LISTS_ID).click()

        try: delete = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.DELETE_LIST))
        except Exception:
            raise

        delete.click()

        self.driver.find_element_by_css_selector(OtherPageLocators.DONE_MANAGE).click()

        """ The below function clicks at an element that opens a new window, handles
        the window and asserts its title"""
    def open_window_assert_title(self, element_locator, page_title):
        self.driver.window_handles
        try: element = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(element_locator))
        except Exception:
            raise
        element.click()
        time.sleep(1)

        self.driver.switch_to_window(self.driver.window_handles[1])                                   # Pop up Handling
        try: assert self.driver.title in page_title
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])


        """ Function that hovers over an element and clicks it."""
    def move_mouse_to_element_and_click(self, element_locator):
        element_to_hover = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(element_locator))
        hover = ActionChains(self.driver).move_to_element(element_to_hover)
        hover.click().perform()


        """ Function that asserts the given currency symbol exists in the currency symbol field."""
    def assert_currency_in_flag(self, symbol):
        self.verificationErrors = []

        currency_symbol = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.CURRENCY_SYMBOL_ID)).text

        try: assert currency_symbol == symbol
        except AssertionError as e: self.verificationErrors.append(str(e))
        print currency_symbol


        """ The function below types in the name of a country so as to change the currency to the one of the given country."""
    def change_currency(self, country):
        country_field = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.CURRENCY_COUNTRY_ID))
        country_field.clear()
        country_field.send_keys(country)
        submit = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.SUBMIT_ID))
        submit.click()


        """ Function below verifies that the currency changed in the price field of the main page."""
    def verify_currency_changed(self, currency_symbol):
        self.verificationErrors = []
        time.sleep(2)

        price = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.PRICE_FIELD)).text
        try: assert currency_symbol in price
        except AssertionError as e: self.verificationErrors.append(str(e))
        print price



        """ Function that gets the cost of a product in order to use it in other asserting functions."""
    def get_cost(self):
        global cost
        original_cost = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.PRICE_FIELD)).text
        cost_without_symbol = (original_cost.replace('$', ' '))
        cost = Decimal(cost_without_symbol)


        """ The below function verifies that the currency of the price in the main screen has been
        altered from USD to Euros."""
    def verify_currency_of_price_changed_to_euro_correctly(self):
        self.verificationErrors = []
        time.sleep(2)

        original_price = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.PRICE_FIELD)).text
        try: assert "" in original_price
        except AssertionError as e: self.verificationErrors.append(str(e))
        print original_price

        price_without_symbol = (original_price.replace('$', ' '))
        price = Decimal(price_without_symbol)
        print "The price is: %f" % price

        correct_price_in_euro = (price * 0.880080)

        if price == correct_price_in_euro:
            print "The USD to EURO converter works as expected. The price is: %f" % price

        else:
            print "The rate is not correct. The converted price is: %f" % price


class HappyCube(MainPage):

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(31)
        self.driver.get("http://www.shapeways.com/product/3PDRJHSFP/a-happy-cube?li=shop-results&optionId=7378234")
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

        """Destructor!"""
    def __del__(self):
        self.driver.close()


    def is_title_matches(self):
        return "Happy Cube" in self.driver.title


    """ In this function we get the data from the fields Favorite by more and total users
            that have favorited the product in order to use it in the favorite verification functions."""
    def fav_status_before_addition(self):
        global favorites_total
        favorites_t = self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL).text              # Favorites total element
        favorites_total = int(favorites_t)


        """ In the function below we get the data of the favorite more and total users after the favorite icon has been pressed.
            This way we will compare the results based on the data that we got in function "fav_status_before_addition"."""
    def fav_status_after_addition(self):
        global favorites_total_plus

        favorites_t_plus = self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL).text             # Favorites total element
        favorites_total_plus = int(favorites_t_plus)



    def verification_of_favorite_total(self):

        assert(favorites_total + 1 == favorites_total_plus)
        print "Favorites total equals: %r , favorites_total_plus equals: %r" % (favorites_total, favorites_total_plus)













