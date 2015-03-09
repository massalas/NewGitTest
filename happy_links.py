import unittest
from selenium import webdriver
from locators import MainPageLocators, OtherPageLocators, HappyPageDict
import Page2, time


class HappyLinks(unittest.TestCase):

    #mylist =[
     #   {"locator" : "MainPageLocators.FORUMS_FOOTER", "title" : "Shapeways 3D Printing Forums", "anchor" : OtherPageLocators.FORUM_ANCHOR, "tag" :"Shapeways"},
      #  {"locator" : "MainPageLocators.EVENTS_FOOTER", "title" : "Shapeways | Events", "anchor" : OtherPageLocators.EVENTS_ANCHOR, "tag" : "Community Events and Meetups"},
       # {"locator" : "MainPageLocators.JOIN_CREW", "title" : "Join the World's Largest 3D Printing Community - Shapeways", "anchor" : OtherPageLocators.JOIN_CREW_ANCHOR, "tag" : "Shapeways 3D Printing Community"},
       # {"locator" : "MainPageLocators.EDUCATION_FOOTER", "title" : "Shapeways Education Program", "anchor" : OtherPageLocators.EDUCATION_ANCHOR, "tag" :"Sign up for Shapeways Education Program to save on your 3D prints and be a part of the world's largest 3D printing community"}
#]





    def setUp(self):
        self.driver = webdriver.Firefox()
        self.happy_cube = Page2.HappyCube(self.driver)
        print "Test Happy_links is running!"
        self.driver.delete_all_cookies()
        assert self.happy_cube.is_title_matches(), "Happy Cube title doesn't match"





    def test_happy_link(self):





        for i in xrange(4):
            self.happy_cube.open_link_from_dict(HappyPageDict.element)



        #self.happy_cube.open_page_and_assert_title(MainPageLocators.FORUMS_FOOTER, "Shapeways 3D Printing Forums",
        #OtherPageLocators.FORUM_ANCHOR, "Shapeways")
        #self.driver.back()
        #print "next test"

        #self.happy_cube.open_page_and_assert_title(MainPageLocators.EVENTS_FOOTER, "Shapeways | Events",
        #OtherPageLocators.EVENTS_ANCHOR, "Community Events and Meetups")
        #self.driver.back()
        #print "next test"

        #self.happy_cube.open_page_and_assert_title(MainPageLocators.JOIN_CREW, "Join the World's Largest 3D Printing Community - Shapeways",
        #OtherPageLocators.JOIN_CREW_ANCHOR, "Shapeways 3D Printing Community")
        #self.driver.back()
        #print "next test"

        #self.happy_cube.open_page_and_assert_title(MainPageLocators.EDUCATION_FOOTER, "Shapeways Education Program",
        #OtherPageLocators.EDUCATION_ANCHOR, "Sign up for Shapeways Education Program to save on your 3D prints and be a part of the world's largest 3D printing community")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()