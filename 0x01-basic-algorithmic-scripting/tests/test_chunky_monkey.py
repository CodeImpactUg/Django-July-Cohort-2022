import unittest


from chunky_monkey import chunkArrayInGroups


class TestChunkArrayInGroups(unittest.TestCase):
    def test_split_list_into_groups(self):
        """
        chunkArrayInGroups(["a", "b", "c", "d"], 2) should return [["a", "b"], ["c", "d"]].
        chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3) should return [[0, 1, 2], [3, 4, 5]].
        chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2) should return [[0, 1], [2, 3], [4, 5]].
        chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4) should return [[0, 1, 2, 3], [4, 5]].
        chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3) should return [[0, 1, 2], [3, 4, 5], [6]].
        chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4) should return [[0, 1, 2, 3], [4, 5, 6, 7], [8]].
        chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2) should return [[0, 1], [2, 3], [4, 5], [6, 7], [8]].
        """
        self.assertEqual(
            chunkArrayInGroups(["a", "b", "c", "d"], 2), [["a", "b"], ["c", "d"]]
        )
        self.assertEqual(
            chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3), [[0, 1, 2], [3, 4, 5]]
        )
        self.assertEqual(
            chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2), [[0, 1], [2, 3], [4, 5]]
        )
        self.assertEqual(
            chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4), [[0, 1, 2, 3], [4, 5]]
        )
        self.assertEqual(
            chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3), [[0, 1, 2], [3, 4, 5], [6]]
        )
        self.assertEqual(
            chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4),
            [[0, 1, 2, 3], [4, 5, 6, 7], [8]],
        )
        self.assertEqual(
            chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2),
            [[0, 1], [2, 3], [4, 5], [6, 7], [8]],
        )


if __name__ == "__main__":
    unittest.main()
