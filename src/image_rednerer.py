from PIL import Image, ImageDraw
import random

class ImageRenderer:
    def __init__(self, style, colors, size=(512, 512)):
        self.style = style
        self.colors = colors
        self.size = size

    def render(self, output_path="generated_art.png"):
        img = Image.new("RGB", self.size, color=self._background_color())
        draw = ImageDraw.Draw(img)

        # Simulate brush strokes or geometric patterns
        for _ in range(200):
            self._draw_random_stroke(draw)

        img.save(output_path)
        print(f"Artwork saved to {output_path}")
        return img

    def _background_color(self):
        return random.choice(self.colors)

    def _draw_random_stroke(self, draw):
        x1, y1 = random.randint(0, self.size[0]), random.randint(0, self.size[1])
        x2, y2 = random.randint(0, self.size[0]), random.randint(0, self.size[1])
        color = random.choice(self.colors)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=random.randint(5, 15))

if __name__ == "__main__":
    # Example Usage
    renderer = ImageRenderer("abstract", ["#3498DB", "#F4D03F", "#E67E22"])
    renderer.render()
