import matplotlib.pyplot as plt
from src.color_palette_generator import ColorPaletteGenerator
from src.image_renderer import ImageRenderer

# Experiment with color palettes
colors = ["blue", "orange", "white"]
palette_generator = ColorPaletteGenerator(colors)
palette = palette_generator.generate_palette()
print("Generated Palette:", palette)

# Generate artwork
renderer = ImageRenderer("abstract", palette)
image = renderer.render("outputs/experiment_art.png")

# Display image
plt.imshow(image)
plt.title("Style Experiment")
plt.axis("off")
plt.show()
