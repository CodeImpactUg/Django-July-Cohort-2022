import unittest


from repeat_string import repeatStringNumTimes


class TestRepeatStringNumTimes(unittest.TestCase):
    def test_repeat_string(self):
        """
        repeatStringNumTimes("*", 3) should return the string ***.
        repeatStringNumTimes("abc", 3) should return the string abcabcabc.
        repeatStringNumTimes("abc", 4) should return the string abcabcabcabc.
        repeatStringNumTimes("abc", 1) should return the string abc.
        repeatStringNumTimes("*", 8) should return the string ********.
        repeatStringNumTimes("abc", -2) should return an empty string ("").
        repeatStringNumTimes("abc", 0) should return "".
        """
        self.assertEqual(repeatStringNumTimes("*", 3), "***")
        self.assertEqual(repeatStringNumTimes("abc", 3), "abcabcabc")
        self.assertEqual(repeatStringNumTimes("abc", 4), "abcabcabcabc")
        self.assertEqual(repeatStringNumTimes("abc", 1), "abc")
        self.assertEqual(repeatStringNumTimes("*", 8), "********")
        self.assertEqual(repeatStringNumTimes("abc", -2), "")
        self.assertEqual(repeatStringNumTimes("abc", 0), "")


if __name__ == "__main__":
    unittest.main()
