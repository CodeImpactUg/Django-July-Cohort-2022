import unittest


from finders_keepers import findElement


class TestFindElement(unittest.TestCase):
    def test_find_element(self):
        """
        findElement([1, 3, 5, 8, 9, 10], function(num) { return num % 2 === 0; }) should return 8.
        findElement([1, 3, 5, 9], function(num) { return num % 2 === 0; }) should return None.
        """
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
