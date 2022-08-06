import unittest


from largest_numbers import largestOfFour


class TestLargestOfFour(unittest.TestCase):
    def test_find_largest_of_four(self):
        """
        largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]) should return an array.

        largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]) should return [27, 5, 39, 1001].
        largestOfFour([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]) should return [9, 35, 97, 1000000].
        largestOfFour([[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]) should return [25, 48, 21, -3].
        """
        self.assertEqual(
            largestOfFour(
                [[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]
            ),
            [27, 5, 39, 1001],
        )
        self.assertEqual(
            largestOfFour(
                [
                    [4, 9, 1, 3],
                    [13, 35, 18, 26],
                    [32, 35, 97, 39],
                    [1000000, 1001, 857, 1],
                ]
            ),
            [9, 35, 97, 1000000],
        )
        self.assertEqual(
            largestOfFour(
                [
                    [17, 23, 25, 12],
                    [25, 7, 34, 48],
                    [4, -10, 18, 21],
                    [-72, -3, -17, -10],
                ]
            ),
            [25, 48, 21, -3],
        )


if __name__ == "__main__":
    unittest.main()
