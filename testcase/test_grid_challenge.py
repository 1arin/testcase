import unittest
from case.grid_challenge import gridChallenge

class GridChallengeTestCase(unittest.TestCase):
    def test_single_row(self):
        grid = ["abcd"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_single_column(self):
        grid = ["a", "b", "c", "d"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_ordered_grid(self):
        grid = ["abc", "def", "ghi"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_unordered_grid(self):
        grid = ["bac", "edf", "ghi"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")


    def test_mixed_grid(self):
        grid = ["axyz", "bcdz", "ghiz"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

if __name__ == '__main__':
    unittest.main()
