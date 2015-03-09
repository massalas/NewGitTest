from locators import MainPageLocators, OtherPageLocators
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
import Page




class HappyCube(Page.MainPage):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://www.shapeways.com/product/3PDRJHSFP/a-happy-cube?li=shop-results&optionId=7378234")
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

        """Destructor!"""
    #def __del__(self):
        # self.driver.close()


    def is_title_matches(self):
        return "Happy Cube" in self.driver.title


    """ In this function we get the data from the fields Favorite by more and total users
            that have favorited the product in order to use it in the favorite verification functions."""
    def fav_status_before_addition(self):
        global favorites_total
        favorites_t = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL)).text              # Favorites total element
        favorites_total = int(favorites_t)


        """ In the function below we get the data of the favorite more and total users after the favorite icon has been pressed.
            This way we will compare the results based on the data that we got in function "fav_status_before_addition"."""
    def fav_status_after_addition(self):
        global favorites_total_plus

        favorites_t_plus = WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(MainPageLocators.FAVORITES_TOTAL)).text             # Favorites total element
        favorites_total_plus = int(favorites_t_plus)



    def verification_of_favorite_total(self):

        assert(favorites_total + 1 == favorites_total_plus)
        print "Favorites total equals: %r , favorites_total_plus equals: %r" % (favorites_total, favorites_total_plus)




    """ Basic function that clicks at a page link and verifies that the page has been loaded by checking the title page. """
    def open_link_from_dict(self, dictionary):
        self.verificationErrors = []
        self.driver.set_page_load_timeout(31)
        #mylist = [
         #   {'locator' : "some locator", 'title' : "some title", 'anchor' : "some anchor", 'tag' : "some tag"},
          #  {'locator' : "some locator", 'title' : "some title", 'anchor' : "some anchor", 'tag' : "some tag"}]


        print "Starting point of test"
        time.sleep(3)





        while True:
            try:

                WebDriverWait(self.driver, 10).until(lambda driver : self.driver.find_element_by_css_selector(dictionary['1'])).is_enabled()           # Page icon
                print "Right before the click"
                page_icon = self.driver.find_element_by_css_selector(dictionary['1']).click()
            except TimeoutException:
                print "Timeout 1, retrying..."
                self.driver.refresh()
                continue
            else:
                break

        while True:
            try:
                print "Here we go!"
                WebDriverWait(self.driver, 5).until(lambda driver : self.driver.find_element_by_css_selector(mylist[2])).is_enabled()
                page_tag = self.driver.find_element_by_css_selector(mylist[2]).text
                if page_tag in mylist[3]:
                    print "Tag verified, tag value is: %s" % page_tag
                else:
                    print "Error! is %s" % page_tag

                if self.driver.title in mylist[1]:
                    print "Title has been asserted and is: %s " % mylist[1]
                else:
                    print "Error! Title is: %r" % self.driver.title
            except TimeoutException:
                print "Timeout 2, retrying..."
                self.driver.refresh()
                continue
            else:
                break

        time.sleep(1)
        print "End of test"
        self.driver.back()




"""
    def utf_8_encoder(unicode_list):
'''
    Covert list that may contain unicode data to utf8
    as csv writer doesn't handle unicode
    @param unicode_list: list with strings
'''
        for i in xrange(len(unicode_list)):
            if isinstance(unicode_list[i], unicode):
                unicode_list[i] = unicode_list[i].encode('utf8')
        return unicode_list"""