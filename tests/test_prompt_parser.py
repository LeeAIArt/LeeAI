import unittest
from src.prompt_parser import PromptParser

class TestPromptParser(unittest.TestCase):
    def test_parse_valid_prompt(self):
        prompt = "Abstract, calm mood, blue and yellow tones"
        parser = PromptParser(prompt)
        result = parser.parse()
        self.assertEqual(result["style"], "abstract")
        self.assertEqual(result["mood"], "calm")
        self.assertIn("blue", result["colors"])

    def test_parse_invalid_prompt(self):
        prompt = "Undefined style with random inputs"
        parser = PromptParser(prompt)
        result = parser.parse()
        self.assertEqual(result["style"], "default_style")
        self.assertEqual(result["mood"], "default_mood")
        self.assertEqual(result["colors"], "default_colors")

if __name__ == '__main__':
    unittest.main()
