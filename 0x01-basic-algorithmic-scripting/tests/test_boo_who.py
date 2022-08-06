import unittest


from boo_who import booWho


class TestBooWho(unittest.TestCase):
    def test_boo_who(self):
        """
        booWho(True) should return True.
        booWho(False) should return True.
        booWho([1, 2, 3]) should return False.
        booWho([]) should return False.
        booWho({ "a": 1 }) should return False.
        booWho(1) should return False.
        booWho(None) should return False.
        booWho("a") should return False.
        booWho("True") should return False.
        booWho("False") should return False.
        booWho("") should return False.
        """
        self.assertTrue(booWho(True))
        self.assertTrue(booWho(False))
        self.assertFalse(booWho([1, 2, 3]))
        self.assertFalse(booWho([]))
        self.assertFalse(booWho({"a": 1}))
        self.assertFalse(booWho(None))
        self.assertFalse(booWho("a"))
        self.assertFalse(booWho("True"))
        self.assertFalse(booWho("False"))
        self.assertFalse(booWho(""))


if __name__ == "__main__":
    unittest.main()
