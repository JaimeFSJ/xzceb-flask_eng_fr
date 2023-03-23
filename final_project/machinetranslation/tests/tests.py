"""
Unit tests
Assert functions english_to_french, french_to_english work properly
"""
import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrenchTranslator(unittest.TestCase):
    def test_english_to_french_translator(self):
        english_text = "Hello"
        english_to_french_translation = english_to_french(english_text)
        self.assertEqual("", "")
        self.assertEqual(english_to_french_translation, "Bonjour")
        self.assertNotEqual(english_to_french_translation, "Hola")

class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_french_to_english_translator(self):
        french_text = "Bonjour"
        french_to_english_translation = french_to_english(french_text)
        self.assertEqual("", "")
        self.assertEqual(french_to_english_translation, "Hello")
        self.assertNotEqual(french_to_english_translation, "Hola")

if __name__ == '__main__':
    unittest.main()
