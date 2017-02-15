#!/usr/bin/env python3
import allure
import pytest
from test_fw_example.pages.google import GooglePage
from test_fw_example.tests.common import BaseTest


@allure.testcase("Simple web test")
class TestGoogle(BaseTest):
    def setup_method(self, method):
        with allure.step("Open google page"):
            self.main_page = GooglePage()
            self.main_page.open()

    @allure.feature("Search feature")
    @pytest.mark.parametrize("text_to_search", ("test", "python"))
    def test_search(self, text_to_search):
        # text_to_search = "test"
        with allure.step("Try to search text: " + text_to_search):
            result_page = self.main_page.search(text_to_search)
            print("Result statistics: " + result_page.statistics.text)
        with allure.step("Check search results"):
            for result in result_page.results:
                assert all(word.text.lower() in text_to_search for word in result.found_words)


if __name__ == '__main__':
    pytest.main()
