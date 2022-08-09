import unittest


from celcius_fahrenheit import convertCtoF


class TestCovertCtoF(unittest.TestCase):
    def test_convert_C_to_F(self):
        self.assertEqual("foo".upper(), "FOO")
        """
        convertCtoF(0) should return a number
        convertCtoF(-30) should return a value of -22
        convertCtoF(-10) should return a value of 14
        convertCtoF(0) should return a value of 32
        convertCtoF(20) should return a value of 68
        convertCtoF(30) should return a value of 86
        """
        self.assertEqual(convertCtoF(-30), -22)
        self.assertEqual(convertCtoF(-10), 14)
        self.assertEqual(convertCtoF(0), 32)
        self.assertEqual(convertCtoF(20), 68)
        self.assertEqual(convertCtoF(30), 86)


if __name__ == "__main__":
    unittest.main()
