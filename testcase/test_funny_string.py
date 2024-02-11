from case.funny_string import funnyString
import unittest

class FunnyStringTestCase(unittest.TestCase):
    def test_funny_string_1(self):
        result = funnyString("acxz")
        self.assertEqual(result, "Funny")

    def test_funny_string_2(self):
        result = funnyString("bcxz")
        self.assertEqual(result, "Not Funny")

    def test_funny_string_3(self):
        result = funnyString("abcde")
        self.assertEqual(result, "Funny")

    def test_funny_string_4(self):
        result = funnyString("abcd")
        self.assertEqual(result, "Not Funny")

    def test_funny_string_5(self):
        result = funnyString("aba")
        self.assertEqual(result, "Funny")

if __name__ == '__main__':
    unittest.main()
