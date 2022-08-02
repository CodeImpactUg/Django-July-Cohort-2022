import unittest

from unittest.mock import MagicMock

from mocking import total


class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        total.read = MagicMock()
        total.read.return_value = [1, 2, 3]
        result = total.calculate_total("file.txt")
        self.assertEqual(result, 6)
