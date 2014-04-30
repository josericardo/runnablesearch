#!/usr/bin/env python
# coding=utf-8

import unittest
import runnablesearch.searcher as search


class SearchTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_can_tell_a_python_script_has_a_main(self):
        self.assertTrue(search.has_main('runnablesearch/tests/examples/file_with_main.py'))

    def test_can_tell_a_python_script_doesnt_have_a_main(self):
        self.assertFalse(search.has_main('runnablesearch/tests/examples/file_without_main.py'))

    def test_can_tell_a_regular_file_doesnt_have_a_main(self):
        self.assertFalse(search.has_main('runnablesearch/tests/examples/not_a_python_file'))
