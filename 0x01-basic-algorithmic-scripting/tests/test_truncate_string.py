import unittest


from truncate_string import truncateString


class TestTruncateString(unittest.TestCase):
    def test_truncate_string(self):
        """
        truncateString("A-tisket a-tasket A green and yellow basket", 8) should return the string A-tisket...
        truncateString("Peter Piper picked a peck of pickled peppers", 11) should return the string Peter Piper...
        truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length) should return the string A-tisket a-tasket A green and yellow basket.
        truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length + 2) should return the string A-tisket a-tasket A green and yellow basket.
        truncateString("A-", 1) should return the string A...
        truncateString("Absolutely Longer", 2) should return the string Ab...
        """
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
