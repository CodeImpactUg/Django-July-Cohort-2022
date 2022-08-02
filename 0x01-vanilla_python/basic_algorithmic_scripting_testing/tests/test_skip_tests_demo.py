"""Skipping Tests
"""

import unittest

from sys import platform


# Skipping tests at method level
class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skip("Work in progress")
    def test_case_2(self):
        pass

    def test_case_3(self):
        self.skipTest("Work in progress")

    def test_case_4(self):
        raise unittest.SkipTest("Work in progress")


# Skipping Tests at class level
@unittest.skip("Work in progress")
class TestDemo2(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertIsNotNone([])


# Skipping a test with a condition
class TestDemo3(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skipIf(platform.startswith("win"), "Do not run on Windows")
    def test_case_2(self):
        self.assertIsNotNone([])
