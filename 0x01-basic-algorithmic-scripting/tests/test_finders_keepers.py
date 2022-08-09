import unittest


from finders_keepers import findElement


class TestFindElement(unittest.TestCase):
    def test_find_element(self):
        """
        findElement([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0) should return 8.
        findElement([1, 3, 5, 9], lambda num: num % 2 == 0) should return None.
        """
        self.assertEqual(findElement([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0), 8)
        self.assertEqual(findElement([1, 3, 5, 9], lambda num: num % 2 == 0), None)


if __name__ == "__main__":
    unittest.main()
