import unittest
from src.color_palette_generator import ColorPaletteGenerator

class TestColorPaletteGenerator(unittest.TestCase):
    def test_generate_palette(self):
        colors = ["blue", "yellow"]
        generator = ColorPaletteGenerator(colors)
        palette = generator.generate_palette()
        self.assertIn("#3498DB", palette)  # Blue HEX
        self.assertIn("#F4D03F", palette)  # Yellow HEX

    def test_generate_empty_palette(self):
        generator = ColorPaletteGenerator([])
        palette = generator.generate_palette()
        self.assertEqual(len(palette), 1)  # Default color palette should have at least one color
        self.assertEqual(palette[0], "#CCCCCC")  # Default gray

if __name__ == '__main__':
    unittest.main()
