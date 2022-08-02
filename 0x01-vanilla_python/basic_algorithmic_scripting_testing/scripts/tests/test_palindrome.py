import unittest

from palindrome import is_palindrome, is_palindrome2


class TestIsPalindrome(unittest.TestCase):
    def test_string_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("radix"))
    
    def test_string_is_palindrome_2(self):
        self.assertTrue(is_palindrome2("radar"))
        self.assertFalse(is_palindrome2("radix"))


if __name__ == "__main__":
    unittest.main()