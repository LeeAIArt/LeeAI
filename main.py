import argparse
from src.art_generator import ArtGenerator
from src.utils import display_image

def main():
    parser = argparse.ArgumentParser(description="Lee AI Art Generator")
    parser.add_argument('--prompt', type=str, required=True, help='Art description prompt')
    args = parser.parse_args()

    # Initialize art generator
    generator = ArtGenerator()
    print(f"Generating art with prompt: '{args.prompt}'")
    output_image = generator.generate(args.prompt)

    # Display output
    display_image(output_image, title="Generated Artwork")

if __name__ == "__main__":
    main()
