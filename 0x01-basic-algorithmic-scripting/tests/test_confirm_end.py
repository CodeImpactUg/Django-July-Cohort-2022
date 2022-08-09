import unittest


from confirm_end import confirmEnding


class TestConfirmEnding(unittest.TestCase):
    def test_confirm_ending(self):
        """
        confirmEnding("Bastian", "n") should return True.
        confirmEnding("Congratulation", "on") should return True.
        confirmEnding("Connor", "n") should return False.
        confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification") should return False.
        confirmEnding("He has to give me a new name", "name") should return True.
        confirmEnding("Open sesame", "same") should return True.
        confirmEnding("Open sesame", "sage") should return False.
        confirmEnding("Open sesame", "game") should return False.
        confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain") should return False.
        confirmEnding("Abstraction", "action") should return True.
        """
        self.assertTrue(confirmEnding("Bastian", "n"))
        self.assertTrue(confirmEnding("Congratulation", "on"))
        self.assertFalse(confirmEnding("Connor", "n"))
        self.assertFalse(
            confirmEnding(
                "Walking on water and developing software from a specification are easy if both are frozen",
                "specification",
            )
        )
        self.assertTrue(confirmEnding("He has to give me a new name", "name"))
        self.assertTrue(confirmEnding("Open sesame", "same"))
        self.assertFalse(confirmEnding("Open sesame", "sage"))
        self.assertFalse(confirmEnding("Open sesame", "game"))
        self.assertFalse(
            confirmEnding(
                "If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing",
                "mountain",
            )
        )
        self.assertTrue(confirmEnding("Abstraction", "action"))


if __name__ == "__main__":
    unittest.main()
