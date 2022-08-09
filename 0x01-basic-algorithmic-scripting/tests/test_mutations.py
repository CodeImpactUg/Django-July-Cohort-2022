import unittest


from mutations import mutation


class TestMutation(unittest.TestCase):
    def test_mutation(self):
        """
        mutation(["hello", "hey"]) should return False.
        mutation(["hello", "Hello"]) should return True.
        mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]) should return True.
        mutation(["Mary", "Army"]) should return True.
        mutation(["Mary", "Aarmy"]) should return True.
        mutation(["Alien", "line"]) should return True.
        mutation(["floor", "for"]) should return True.
        mutation(["hello", "neo"]) should return False.
        mutation(["voodoo", "no"]) should return False.
        mutation(["ate", "date"]) should return False.
        mutation(["Tiger", "Zebra"]) should return False.
        mutation(["Noel", "Ole"]) should return True.
        """
        self.assertFalse(mutation(["hello", "hey"]))
        self.assertTrue(mutation(["hello", "Hello"]))
        self.assertTrue(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]))
        self.assertTrue(mutation(["Mary", "Army"]))
        self.assertTrue(mutation(["Alien", "line"]))
        self.assertTrue(mutation(["floor", "for"]))
        self.assertFalse(mutation(["hello", "neo"]))
        self.assertFalse(mutation(["voodoo", "no"]))
        self.assertFalse(mutation(["ate", "date"]))
        self.assertFalse(mutation(["Tiger", "Zebra"]))
        self.assertTrue(mutation(["Noel", "Ole"]))


if __name__ == "__main__":
    unittest.main()
