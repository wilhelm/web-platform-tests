# -*- mode: python; fill-column: 100; comment-column: 100; -*-

import os
import sys
import unittest

# TODO: Should we always include these guys for WPT?
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import base_test


class FancyExampleTest(base_test.WebDriverBaseTest):

    def test_onclick_handler_on_button(self):

        self.driver.get(self.webserver.where_is("examples/res/onclick.html"))
        button = self.driver.find_element_by_css_selector("button")
        result = self.driver.find_element_by_css_selector("#result")

        button.click()
        self.assertEquals("PASS", result.text)


    def test_hover_changes_background(self):

        self.driver.get(self.webserver.where_is("examples/res/hover.html"))

        ref = self.driver.find_element_by_css_selector(".ref")
        test = self.driver.find_element_by_css_selector(".test")

        ActionChains(self.driver) \
          .move_to_element(test) \
          .perform()

        # TODO: Take screenshot of .ref and .test & compare.


if __name__ == "__main__":
    unittest.main()
