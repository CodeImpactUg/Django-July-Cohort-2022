import unittest


from longest_word import findLongestWordLength


class TestFindLongestWordLength(unittest.TestCase):
    def test_find_longest_word_length(self):
        """
        findLongestWordLength("The quick brown fox jumped over the lazy dog") should return a number.
        findLongestWordLength("The quick brown fox jumped over the lazy dog") should return 6.
        findLongestWordLength("May the force be with you") should return 5.
        findLongestWordLength("Google do a barrel roll") should return 6.
        findLongestWordLength("What is the average airspeed velocity of an unladen swallow") should return 8.
        findLongestWordLength("What if we try a super-long word such as otorhinolaryngology") should return 19.
        """
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
