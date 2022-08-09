import unittest
from unittest.mock import patch
import mocking


class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        # start patching
        patcher = patch("mocking.total.read")

        # create a mock object
        mock_read = patcher.start()

        # assign the return value
        mock_read.return_value = [1, 2, 3]

        # test the calculate_total
        result = mocking.total.calculate_total("")
        self.assertEqual(result, 6)

        # stop patching
        patcher.stop()
