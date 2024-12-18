import unittest
from src.art_generator import ArtGenerator

class TestArtGenerator(unittest.TestCase):
    def test_generate_art(self):
        generator = ArtGenerator()
        prompt = "Abstract, vibrant colors"
        image = generator.generate(prompt)
        self.assertEqual(image.size, (512, 512))  # Default size for generated images

    def test_generate_with_empty_prompt(self):
        generator = ArtGenerator()
        image = generator.generate("")
        self.assertEqual(image.size, (512, 512))  # Ensure default image generation

if __name__ == '__main__':
    unittest.main()
