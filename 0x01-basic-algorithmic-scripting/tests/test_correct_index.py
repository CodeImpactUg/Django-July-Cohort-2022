import unittest


from correct_index import getIndexToIns


class TestGetIndexToIns(unittest.TestCase):
    def test_get_correct_index_after_sorting(self):
        """
        getIndexToIns([10, 20, 30, 40, 50], 35) should return 3.
        getIndexToIns([10, 20, 30, 40, 50], 35) should return a number.
        getIndexToIns([10, 20, 30, 40, 50], 30) should return 2.
        getIndexToIns([10, 20, 30, 40, 50], 30) should return a number.
        getIndexToIns([40, 60], 50) should return 1.
        getIndexToIns([40, 60], 50) should return a number.
        getIndexToIns([3, 10, 5], 3) should return 0.
        getIndexToIns([3, 10, 5], 3) should return a number.
        getIndexToIns([5, 3, 20, 3], 5) should return 2.
        getIndexToIns([5, 3, 20, 3], 5) should return a number.
        getIndexToIns([2, 20, 10], 19) should return 2.
        getIndexToIns([2, 20, 10], 19) should return a number.
        getIndexToIns([2, 5, 10], 15) should return 3.
        getIndexToIns([2, 5, 10], 15) should return a number.
        getIndexToIns([], 1) should return 0.
        getIndexToIns([], 1) should return a number.
        """
        self.assertEqual(getIndexToIns([10, 20, 30, 40, 50], 35), 3)
        self.assertEqual(getIndexToIns([10, 20, 30, 40, 50], 30), 2)
        self.assertEqual(getIndexToIns([40, 60], 50), 1)
        self.assertEqual(getIndexToIns([3, 10, 5], 3), 0)
        self.assertEqual(getIndexToIns([5, 3, 20, 3], 5), 2)
        self.assertEqual(getIndexToIns([2, 20, 10], 19), 2)
        self.assertEqual(getIndexToIns([2, 5, 10], 15), 3)
        self.assertEqual(getIndexToIns([], 1), 0)


if __name__ == "__main__":
    unittest.main()
