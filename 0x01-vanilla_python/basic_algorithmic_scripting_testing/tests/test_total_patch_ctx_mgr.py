import unittest
from unittest.mock import patch

import mocking


class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        with patch("mocking.total.read") as mock_read:
            mock_read.return_value = [1, 2, 3]
            result = mocking.total.calculate_total("")
            self.assertEqual(result, 6)
