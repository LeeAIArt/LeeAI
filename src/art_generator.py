import torch
from torchvision import transforms
from PIL import Image
import random

class ArtGenerator:
    def __init__(self, model_path="models/pretrained_model.pth"):
        self.model = torch.load(model_path, map_location=torch.device('cpu'))
        self.device = torch.device("cpu")
        self.model.eval()

    def generate(self, prompt):
        # Simulate using prompt for art generation
        print(f"Interpreting prompt: '{prompt}'")
        torch.manual_seed(hash(prompt) % 1000)  # Random seed for diversity
        image = self._generate_random_image()
        return image

    def _generate_random_image(self):
        # Simulate art creation process with placeholder image
        width, height = 512, 512
        image = Image.new("RGB", (width, height), color=self._random_color())
        return image

    @staticmethod
    def _random_color():
        return tuple(random.randint(0, 255) for _ in range(3))
