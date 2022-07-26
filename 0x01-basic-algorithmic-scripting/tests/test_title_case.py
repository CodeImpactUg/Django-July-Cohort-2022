import unittest


from title_case import titleCase


class TestTitleCase(unittest.TestCase):
    def test_title_case_sentence(self):
        """
        titleCase("I'm a little tea pot") should return a string.
        titleCase("I'm a little tea pot") should return the string I'm A Little Tea Pot.
        titleCase("sHoRt AnD sToUt") should return the string Short And Stout.
        titleCase("HERE IS MY HANDLE HERE IS MY SPOUT") should return the string Here Is My Handle Here Is My Spout.
        """
        self.assertEqual(titleCase("I'm a little tea pot"), "I'm A Little Tea Pot")
        self.assertEqual(titleCase("sHoRt AnD sToUt"), "Short And Stout")
        self.assertEqual(
            titleCase("HERE IS MY HANDLE HERE IS MY SPOUT"),
            "Here Is My Handle Here Is My Spout",
        )


if __name__ == "__main__":
    unittest.main()
