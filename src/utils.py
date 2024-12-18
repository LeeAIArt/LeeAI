from PIL import Image
import matplotlib.pyplot as plt

def display_image(image, title="Image"):
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()

def save_image(image, path):
    image.save(path)
    print(f"Image saved to {path}")
