import unittest
from  case.two_characters import alternate

class AlternateTestCase(unittest.TestCase):
    def test_empty_string(self):
        result = alternate("")
        self.assertEqual(result, 0)

    def test_single_character_string(self):
        result = alternate("a")
        self.assertEqual(result, 0)

    def test_string_with_same_characters(self):
        result = alternate("aaaa")
        self.assertEqual(result, 0)

    def test_string_with_two_distinct_characters(self):
        result = alternate("ab")
        self.assertEqual(result, 2)

    def test_string_with_multiple_distinct_characters(self):
        result = alternate("abca")
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
