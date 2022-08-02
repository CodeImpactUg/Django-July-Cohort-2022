import unittest

from array_sum import list_sum, list_sum2


class TestListSum(unittest.TestCase):
    def test_sum_list_elements(self):
        self.assertEqual(list_sum([1, 2, 3]), 6)
        self.assertEqual(list_sum([15, 12, 13, 10]), 50)
        self.assertEqual(list_sum([]), 0)
    
    def test_sum_list_elements_2(self):
        self.assertEqual(list_sum2([1, 2, 3]), 6)
        self.assertEqual(list_sum2([15, 12, 13, 10]), 50)
        self.assertEqual(list_sum2([]), 0)


if __name__ == "__main__":
    unittest.main()
