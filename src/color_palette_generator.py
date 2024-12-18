import random

class ColorPaletteGenerator:
    def __init__(self, colors):
        self.colors = colors if isinstance(colors, list) else [colors]

    def generate_palette(self):
        base_colors = self.colors
        palette = [self._adjust_color(c) for c in base_colors]
        return palette

    def _adjust_color(self, color):
        color_shades = {
            "red": "#FF5733", "blue": "#3498DB", "yellow": "#F4D03F",
            "green": "#28B463", "orange": "#E67E22", "black": "#1C2833",
            "white": "#FBFCFC"
        }
        return color_shades.get(color, "#CCCCCC")

if __name__ == "__main__":
    # Example Usage
    generator = ColorPaletteGenerator(["blue", "yellow"])
    print(generator.generate_palette())  # Output: ['#3498DB', '#F4D03F']
