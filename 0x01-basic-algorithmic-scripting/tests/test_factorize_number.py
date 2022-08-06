import unittest


from factorize_number import factorialize


class TestFactorizeNumber(unittest.TestCase):
    def test_factorize(self):
        """
        factorialize(5) should return a number.
        factorialize(5) should return 120.
        factorialize(10) should return 3628800.
        factorialize(20) should return 2432902008176640000.
        factorialize(0) should return 1.
        """
        self.assertEqual(factorialize(5), 120)
        self.assertEqual(factorialize(10), 3628800)
        self.assertEqual(factorialize(20), 2432902008176640000)
        self.assertEqual(factorialize(0), 1)


if __name__ == "__main__":
    unittest.main()
