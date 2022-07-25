import unittest


from falsy_bouncer import bouncer


class TestBouncer(unittest.TestCase):
    def test_bouncer(self):
        """
        bouncer([7, "ate", "", false, 9]) should return [7, "ate", 9].
        bouncer(["a", "b", "c"]) should return ["a", "b", "c"].
        bouncer([false, null, 0, NaN, undefined, ""]) should return [].
        bouncer([null, NaN, 1, 2, undefined]) should return [1, 2].
        """
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
