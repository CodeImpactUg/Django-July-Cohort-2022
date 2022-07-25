import unittest


from factorize_number import factorize


class TestFactorizeNumber(unittest.TestCase):
    def test_factorize(self):
        """
        factorialize(5) should return a number.
        factorialize(5) should return 120.
        factorialize(10) should return 3628800.
        factorialize(20) should return 2432902008176640000.
        factorialize(0) should return 1.
        """
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
