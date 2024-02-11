from case.caesar_cipher import caesarCipher
import unittest

class CaesarCipherTestCase(unittest.TestCase):
    def test_lowercase_rotation(self):
        result = caesarCipher("abc", 1)
        self.assertEqual(result, "bcd")

    def test_uppercase_rotation(self):
        result = caesarCipher("XYZ", 2)
        self.assertEqual(result, "ZAB")

    def test_mixedcase_rotation(self):
        result = caesarCipher("AbC", 3)
        self.assertEqual(result, "DeF")

    def test_special_characters(self):
        result = caesarCipher("!@#", 5)
        self.assertEqual(result, "!@#")

    def test_large_rotation(self):
        result = caesarCipher("abcXYZ", 26)
        self.assertEqual(result, "abcXYZ")

if __name__ == '__main__':
    unittest.main()
