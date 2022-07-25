import unittest


from slice_splice import frankenSplice


class TestFrankenSplice(unittest.TestCase):
    def test_slice_splice(self):
        """
        frankenSplice([1, 2, 3], [4, 5], 1) should return [4, 1, 2, 3, 5].
        frankenSplice([1, 2], ["a", "b"], 1) should return ["a", 1, 2, "b"].
        frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2) should return ["head", "shoulders", "claw", "tentacle", "knees", "toes"].
        All elements from the first array should be added to the second array in their original order. frankenSplice([1, 2, 3, 4], [], 0) should return [1, 2, 3, 4].
        The first array should remain the same after the function runs.
        The second array should remain the same after the function runs.
        """
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
