import unittest
from src.image_renderer import ImageRenderer
from PIL import Image

class TestImageRenderer(unittest.TestCase):
    def test_render_image(self):
        renderer = ImageRenderer("abstract", ["#3498DB", "#F4D03F"], size=(256, 256))
        output_path = "outputs/test_art.png"
        image = renderer.render(output_path)
        self.assertTrue(isinstance(image, Image.Image))  # Check if output is a PIL Image
        self.assertEqual(image.size, (256, 256))

    def test_render_invalid_colors(self):
        renderer = ImageRenderer("abstract", [], size=(256, 256))
        output_path = "outputs/test_art_invalid.png"
        image = renderer.render(output_path)
        self.assertTrue(isinstance(image, Image.Image))  # Check if output is a PIL Image
        self.assertEqual(image.size, (256, 256))  # Default size

if __name__ == '__main__':
    unittest.main()
