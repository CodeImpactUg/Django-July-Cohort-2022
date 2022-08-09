import unittest


from reverse_string import reverseString


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        """
        reverseString("hello") should return a string.
        reverseString("hello") should return the string olleh.
        reverseString("Howdy") should return the string ydwoH.
        reverseString("Greetings from Earth") should return the string htraE morf sgniteerG.
        """
        self.assertEqual(reverseString("hello"), "olleh")
        self.assertEqual(reverseString("Howdy"), "ydwoH")
        self.assertEqual(reverseString("Greetings from Earth"), "htraE morf sgniteerG")


if __name__ == "__main__":
    unittest.main()
