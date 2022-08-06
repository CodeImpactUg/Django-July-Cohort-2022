import unittest


from falsy_bouncer import bouncer


class TestBouncer(unittest.TestCase):
    def test_bouncer(self):
        """
        bouncer([7, "ate", "", False, 9]) should return [7, "ate", 9].
        bouncer(["a", "b", "c"]) should return ["a", "b", "c"].
        bouncer([False, None, 0, None, None, ""]) should return [].
        bouncer([None, None, 1, 2, None]) should return [1, 2].
        """
        self.assertEqual(bouncer([7, "ate", "", False, 9]), [7, "ate", 9])
        self.assertEqual(bouncer(["a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(bouncer([False, None, 0, None, None, ""]), [])
        self.assertEqual(bouncer([None, None, 1, 2, None]), [1, 2])


if __name__ == "__main__":
    unittest.main()
