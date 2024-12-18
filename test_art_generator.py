import unittest
from src.art_generator import ArtGenerator

class TestArtGenerator(unittest.TestCase):
    def test_generate_output(self):
        generator = ArtGenerator()
        result = generator.generate("abstract, bold colors")
        self.assertEqual(result.size, (512, 512))

if __name__ == '__main__':
    unittest.main()
