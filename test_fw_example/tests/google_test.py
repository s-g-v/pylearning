#!/usr/bin/env python3

import pytest
from test_fw_example.pages.google import GooglePage
from test_fw_example.tests.common import BaseTest


class TestGoogle(BaseTest):
    def setup_method(self, method):
        self.main_page = GooglePage()
        self.main_page.open()

    def test_search(self):
        #Add test description
        text_to_search = "test"
        #Add step description
        result_page = self.main_page.search(text_to_search)
        print("Result statistics: " + result_page.statistics.text)
        #Add step description
        for result in result_page.results:
            assert all(word.text.lower() in text_to_search for word in result.found_words)


if __name__ == '__main__':
    pytest.main()
