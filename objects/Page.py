from config.locators import MainPageLocators, OtherPageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from decimal import Decimal
from threading import Timer
import time
import os
import sys

class MainPage(object):


    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.shapeways.com/product/DM8QHNHJS/taphandle?optionId=7360379")
        self.driver.maximize_window()
        #self.driver.delete_all_cookies()
        self.verificationErrors = []
        self.accept_next_alert = True


    #    """Destructor!"""
    #def __del__(self):
        # self.driver.close()

        """ Setup to be used when cross browser testing takes place """
#    def setUp(self):
        # self.driver = webdriver.Firefox()

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


    def log(self, msg):
        """ Function for logging events. """
        print (time.strftime("%H:%M:%S") + ": " + msg)


    def is_title_matches(self):
        return "TapHandle" in self.driver.title

    def assert_title_matches(self, some_title):
        return some_title in self.driver.title

    def assert_page_has_been_accessed(self, anchor, tag):

        while True:
            try:
                print "Here we go!"
                WebDriverWait(self.driver, 15).until(lambda driver : self.driver.find_element_by_css_selector(anchor)).is_enabled()
                page_tag = self.driver.find_element_by_css_selector(anchor).text
                #page_tag = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, tag))).text
                if page_tag in tag:
                    print "Tag verified, tag value is: %s" % page_tag
                else:
                    print "Error! is %s" % page_tag
            except TimeoutException:
                print "Timeout 2, retrying..."
                self.driver.refresh()
                continue
            else:
                break

    def tab_back(self):
        self.driver.back()

    def is_element_present(self, how, what):
        try: WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element(by=how, value=what))
        except NoSuchElementException, e: return False
        return True

    def wait_for_element_by_css(self, element_css, timeout):
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_css)))
        except TimeoutException:
            return None

        """ Simply clicks at an element using the css selector. """
    def click_element(self, link):
        element = self.driver.find_element_by_css_selector(link)
        element.click()


    """ Simply clicks at an element using id. """
    def click_element_by_id(self, link):
        element = self.driver.find_element_by_id(link)
        element.click()

    """ Deletion of cookies. """
    def delete_cookies(self):
        self.driver.delete_all_cookies()

        """ Simply selects the SignIN link of main page. """
    def click_sign_in_link(self):
        sign_in = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.SIGN_IN_LINK))
        sign_in.click()




    def spin_assert(self, msg, assertion):
        for i in xrange(60):
            try:
                self.assertTrue(assertion())
                return
            except Exception, e:
                pass
        sleep(1)
        self.fail(msg)


    def wait_for_text_present(self, text, msg=None):
        msg = msg or " waiting for text %s to appear" % text
        assertion = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(element_locator))

        assertion = lambda: self.selenium.is_text_present(text)
        self.spin_assert(msg, assertion)





    def is_submenu_displayed(self):
		return self.is_element_visible(self._zones_submenu_locator)

    def open_zones_menu(self):
        zones_menu = self.selenium.find_element(*self._zones_menu_locator)
        ActionChains(self.selenium).move_to_element(zones_menu).perform()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_zones_submenu_displayed)


        """ Function LOGIN. """
    def login(self):
        username_mass = "mxll"
        pass_mass = "fornaroli1978van"
        user_name = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.USER_NAME_FIELD))
        user_name.clear()
        user_name.send_keys(username_mass)
        password = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.PASSWORD_FIELD))
        password.clear()
        password.send_keys(pass_mass)
        login_button = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.LOGIN_BUTTON))
        login_button.click()



        """ Function LOGOUT """
    def logout(self):
        element_to_hover_over = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MainPageLocators.DROPDOWN_ARROW)))            # Drop down arrow

        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

        sign_out = WebDriverWait(self.driver, 15).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.SIGN_OUT)).click()          # Sign out element



    def check_cart_is_present(self):
        global cart_count
        try:
            self.driver.find_element_by_id(MainPageLocators.CART_COUNT_ID).is_displayed()
            cart = WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.CART_COUNT_ID)).text
            cart_count = int(cart)
            print "Already checked items total is :%r" % cart_count
            return True
        except NoSuchElementException:
            cart_count = 0
            print cart_count







        """ Selects the buy button of the main page and then the checkout icon of the cart pop-up. """
    def buy(self):
        price = self.driver.find_element_by_css_selector(MainPageLocators.PRICE_FIELD).text          # Price on top of buy button
        price = (price.replace('$', ' '))
        price = Decimal(price)

        buy = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.BUY_BUTTON))          # Buy now button
        buy.click()

        new_cart = WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.CART_COUNT_ID)).text
        new_cart_count = int(new_cart)


        if (cart_count + 1) == new_cart_count:
            print "correct"
        else:
            print "Error values are: %r and %r" % (cart_count, new_cart_count)
            #assert (cart_count + 1) == new_cart_count
            #print "Addition of item has been asserted!"

        sub_total = self.driver.find_element_by_css_selector(MainPageLocators.SUBTOTAL).text            # Subtotal element on the top right corner inside the pop-up
        sub_total = (sub_total.replace('$', ' '))
        sub_total = Decimal(sub_total)
        print "Subtotal is: %f" % sub_total
        total = (new_cart_count * price)
        total = Decimal(total)

        if total == sub_total:
            print "Values are the same!"
        elif total != sub_total:
            print "Oh noooooooooooooo"


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
        self.driver.set_page_load_timeout(30)

        for i in xrange(60):
            try: wish_tab = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_TAB))
            except AssertionError as e: self.verificationErrors.append(str(e))

        wish_tab.click()

        for i in xrange(60):
            try: wish_image = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_IMAGE))
            except AssertionError as e: self.verificationErrors.append(str(e))



        #try: wish_tab = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_TAB))
        #except Exception:
        #    raise

        #wish_tab.click()

        #try: wish_image = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_IMAGE))
        #except Exception:
        #    raise




        """ In this function we get the data from the fields Favorite by more and total users
            that have favorited the product in order to use it in the favorite verification functions."""
    def fav_status_before_addition(self):
        global favorites_more, favorites_total
        favorites_m = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITED_MORE)).text              # Favorited by more element
        favorites_more = int(favorites_m)
        favorites_t = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL)).text             # Favorites total element
        favorites_total = int(favorites_t)


        """ In the function below we get the data of the favorite more and total users after the favorite icon has been pressed.
            This way we will compare the results based on the data that we got in function "fav_status_before_addition"."""
    def fav_status_after_addition(self):
        global favorites_more_plus, favorites_total_plus
        self.log("Taking screenshot after the favorite selection: '1_favorite_added.png'")
        self.driver.save_screenshot(r'C:\NewGitTest\Pics\1_favorite_added.png')

        # self.driver.get_screenshot_as_file('/desktop/google.png')


        favorites_m_plus = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITED_MORE)).text              # Favorited by more element
        favorites_more_plus = int(favorites_m_plus)
        favorites_t_plus = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL)).text             # Favorites total element
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
        WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.DROPDOWN_ARROW)).click()           # Drop down arrow element
        WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAV_N_WISHLIST)).click()       # Favorites & Wishlist element



        """ Removes favorite product from the Favorite & Wishlist page. """
    def favorite_remove(self, white, black):

        if self.is_element_present(By.CSS_SELECTOR, white):
            remove_white = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WHITE_REMOVE)).click()
            print "White product has been removed!"
        elif white == "none":
            print "Nothing to remove."
        else:
            return False

        if self.is_element_present(By.CSS_SELECTOR, black):
            remove_black = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.BLACK_REMOVE)).click()
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
        try: image = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.WISH_IMAGE)).is_displayed          # Wishlist image
        except Exception:
            raise

        try: remove = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.REMOVE_FAVORITE))          # Remove favorite n wishlist button
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

    def search_window_with_title_containing(self, string):
        print "search started"
        assert self.driver.title in string

        full_title = self.driver.title
        return full_title
        print "Assertion completed. Title is: %s" % full_title


    def wait_for_page_to_load(self, string_in_title, timeout):
        print "Wait started"
        initial_timeout = timeout
        full_title = self.search_window_with_title_containing(string_in_title)
        while (full_title == '0') and (timeout > 0):
            timeout -= 0.5
            time.sleep(0.5)
            full_title = self.search_window_with_title_containing(string_in_title)
        if timeout == 0:
            raise Exception('Window with title containing "%s" did not appear in %ds.' %(string_in_title, initial_timeout))
        else:
            return full_title
            self.driver.back()


        """ Basic function that clicks at a page link and verifies that the page has been loaded by checking the title page. """
    def open_page_and_assert_title(self, element_locator, page_title, tag, tag_name):
        self.verificationErrors = []
        #self.driver.delete_all_cookies()
        self.driver.set_page_load_timeout(31)


        print "Starting point of test"
        time.sleep(3)

        while True:
            try:
                WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(element_locator)).is_enabled()           # Page icon
                print "Right before the click"
                page_icon = self.driver.find_element_by_css_selector(element_locator).click()
                #except AssertionError as e: self.verificationErrors.append(str(e))
                #time.sleep(1)
                #page_icon.click()
            except TimeoutException:
                print "Timeout 1, retrying..."
                self.driver.refresh()
                continue
            else:
                break

        while True:
            try:
                #t = Timer(50, self.driver.refresh())
                #t.start() # start timer
                print "Here we go!"
                WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_css_selector(tag)).is_enabled()
                page_tag = self.driver.find_element_by_css_selector(tag).text
                #page_tag = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, tag))).text
                if page_tag in tag_name:
                    print "Tag verified, tag value is: %s" % page_tag
                else:
                    print "Error! is %s" % page_tag

                if self.driver.title in page_title:
                    print "Title has been asserted and is: %s " % page_title
                else:
                    print "Error! Title is: %r" % self.driver.title
                #time.sleep(1)
                #self.driver.back()
                #print t
                #t.cancel() # cancel timer
            except TimeoutException:
                print "Timeout 2, retrying..."
                self.driver.refresh()
                continue
            else:
                break

        time.sleep(1)
        print "End of test"
        #self.driver.back()




    """ This function finds an element by its link text, clicks it and verifies that the page has been loaded by checking the title page. """
    def open_page_by_link_text(self, element_locator, page_title, tag, tag_name):
        self.verificationErrors = []
        #self.driver.delete_all_cookies()
        self.driver.set_page_load_timeout(31)


        print "Starting point of test"
        time.sleep(3)

        while True:
            try:
                WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_link_text(element_locator)).is_enabled()           # Page icon
                print "Right before the click"
                page_icon = self.driver.find_element_by_link_text(element_locator).click()
                #except AssertionError as e: self.verificationErrors.append(str(e))
                #time.sleep(1)
                #page_icon.click()
            except TimeoutException:
                print "Timeout 1, retrying..."
                self.driver.refresh()
                continue
            else:
                break

        while True:
            try:
                #t = Timer(50, self.driver.refresh())
                #t.start() # start timer
                print "Here we go!"
                WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_css_selector(tag)).is_enabled()
                page_tag = self.driver.find_element_by_css_selector(tag).text
                #page_tag = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, tag))).text
                if page_tag in tag_name:
                    print "Tag verified, tag value is: %s" % page_tag
                else:
                    print "Error! is %s" % page_tag

                if self.driver.title in page_title:
                    print "Title has been asserted and is: %s " % page_title
                else:
                    print "Error! Title is: %r" % self.driver.title
                #time.sleep(1)
                #self.driver.back()
                #print t
                #t.cancel() # cancel timer
            except TimeoutException:
                print "Timeout 2, retrying..."
                self.driver.refresh()
                continue
            else:
                break

        time.sleep(1)
        print "End of test"
        #self.driver.back()



        """ This function opens the drop down menu at the top right and verifies that the selected option has been loaded"""
    def drop_down(self, element_locator, page_title, tag, tag_name):

        time.sleep(2)
        element_to_hover_over = WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.DROPDOWN_ARROW))           # Drop down arrow

        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        element_to_hover_over.click()


        #while True:
            #try:
        drop_option = WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_css_selector(element_locator)).click()         # Drop down element
            #except Exception:
                #raise


            #try:
        home_tag = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(tag)).text           # Tag locator
            #except Exception:
                #raise


        if home_tag == tag_name:
            print "Tag verified, tag value is: %s" % home_tag
        else:
            print "Error! is %s" % home_tag

        assert self.driver.title in page_title
        print self.driver.title


    def open_tab_and_assert_title(self, element_locator, page_title):
        """ Function below opens the tab and verifies that it has been loaded correctly."""
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
        try: list_icon = WebDriverWait(self.driver, 20).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.ADD_TO_LIST))
        except Exception:
            raise

        list_icon.click()

        time.sleep(1)

        try: list_field = WebDriverWait(self.driver, 20).until(lambda driver : self.driver.find_element_by_id(OtherPageLocators.ADD_LIST_FIELD))
        except Exception:
            raise

        list_field.send_keys("Test!")

        create = WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_id(OtherPageLocators.CREATE_LIST_BUTTON))
        create.click()
        done = WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_id(OtherPageLocators.DONE_LIST_BUTTON_ID))
        done.click()


        """ Verifies that list appears in the drop down menu of the Fav & Wishlist page."""
    def verification_of_list(self):
        try: list_drop_down = WebDriverWait(self.driver, 20).until(lambda driver : self.driver.find_element_by_id(OtherPageLocators.OTHER_LISTS_ID))
        except Exception:
            raise

        list_drop_down.click()

        try: test_list = WebDriverWait(self.driver, 20).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.LIST_DROP_DOWN))
        except Exception:
            raise


        """ Deletion of the created list from the manage list menu."""
    def delete_list(self):
        manage_lists = WebDriverWait(self.driver, 20).until(lambda driver : self.driver.find_element_by_id(OtherPageLocators.MANAGE_LISTS_ID)).click()

        try: delete = WebDriverWait(self.driver, 20).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.DELETE_LIST))
        except Exception:
            raise

        delete.click()

        done = WebDriverWait(self.driver, 20).until(lambda driver : self.driver.find_element_by_css_selector(OtherPageLocators.DONE_MANAGE)).click()


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
    def change_currency_to_country(self, country):
        country_field = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.CURRENCY_COUNTRY_ID))
        country_field.click()


        country_field.send_keys(country)
        time.sleep(1)
        submit = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.SUBMIT_ID))
        submit.click()
        time.sleep(2)


    def encode(self, currency):
        global symbol_encoded

        if type(currency) == str:
        # Ignore errors even if the string is not proper UTF-8 or has
        # broken marker bytes.
        # Python built-in function unicode() can do this.
            symbol_encoded = currency.encode("ascii", "replace")

           # symbol_encoded = unicode(currency, "utf-8", errors="ignore")
        else:
        # Assume the value object has proper __unicode__() method
            symbol_encoded = unicode(currency)




        # self.driver(currency).encode('ascii')

        """ Function below verifies that the currency changed in the price field of the main page."""
    def verify_currency_changed(self):
        self.verificationErrors = []
        time.sleep(2)
        self.move_mouse_to_element_and_click(MainPageLocators.COUNTRY_FLAG)

        currency_symbol = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_id(MainPageLocators.CURRENCY_SYMBOL_ID)).text

        self.encode(currency_symbol)



        price = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.PRICE_FIELD)).text
        try: assert symbol_encoded in price
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
        # try: assert "" in original_price
        # except AssertionError as e: self.verificationErrors.append(str(e))
        # print original_price

        price_without_symbol = (original_price.replace('?', ' '))
        price = Decimal(price_without_symbol)
        print "The price is: %f" % price

        correct_price_in_euro = (cost * 0.880080)

        if price == correct_price_in_euro:
            print "The USD to EURO converter works as expected. The price is: %f" % price

        else:
            print "The rate is not correct. The converted price is: %f" % price















