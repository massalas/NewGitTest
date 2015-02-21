import unittest

import test_add_favorite
import test_buy
import test_open_mid_pages
import test_dropdown_options
import test_open_company_footer
import test_open_top_pages
import test_open_help_footer
import test_open_social_footer
import test_open_legal_footer
import test_open_top_left_pages
import test_add_wishlist
import test_add_list
import test_click_question
import test_social_media
import test_all_the_things


def suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromModule(test_buy)
    test_suite.addTest(test_loader.loadTestsFromModule(test_add_favorite))
    test_suite.addTest(test_loader.loadTestsFromModule(test_open_mid_pages))
    test_suite.addTest(test_loader.loadTestsFromModule(test_dropdown_options))
    test_suite.addTest(test_loader.loadTestsFromModule(test_open_company_footer))
    test_suite.addTest(test_loader.loadTestsFromModule(test_open_top_pages))
    test_suite.addTest(test_loader.loadTestsFromModule(test_open_help_footer))
    test_suite.addTest(test_loader.loadTestsFromModule(test_open_social_footer))
    test_suite.addTest(test_loader.loadTestsFromModule(test_open_legal_footer))
    test_suite.addTest(test_loader.loadTestsFromModule(test_open_top_left_pages))
    test_suite.addTest(test_loader.loadTestsFromModule(test_add_wishlist))
    test_suite.addTest(test_loader.loadTestsFromModule(test_add_list))
    test_suite.addTest(test_loader.loadTestsFromModule(test_click_question))
    test_suite.addTest(test_loader.loadTestsFromModule(test_social_media))
    test_suite.addTest(test_loader.loadTestsFromModule(test_all_the_things))

    return test_suite

my_suite = suite()

runner = unittest.TextTestRunner()
runner.run(my_suite)

