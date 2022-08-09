import unittest


from slice_splice import frankenSplice


class TestFrankenSplice(unittest.TestCase):
    def test_slice_splice(self):
        """
        frankenSplice([1, 2, 3], [4, 5], 1) should return [4, 1, 2, 3, 5].
        frankenSplice([1, 2], ["a", "b"], 1) should return ["a", 1, 2, "b"].
        frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2) should return ["head", "shoulders", "claw", "tentacle", "knees", "toes"].
        frankenSplice([1, 2, 3, 4], [], 0) should return [1, 2, 3, 4].
        The first array should remain the same after the function runs.
        The second array should remain the same after the function runs.
        """
        self.assertEqual(frankenSplice([1, 2, 3], [4, 5], 1), [4, 1, 2, 3, 5])
        self.assertEqual(frankenSplice([1, 2], ["a", "b"], 1), ["a", 1, 2, "b"])
        self.assertEqual(
            frankenSplice(
                ["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2
            ),
            ["head", "shoulders", "claw", "tentacle", "knees", "toes"],
        )
        self.assertEqual(frankenSplice([1, 2, 3, 4], [], 0), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
