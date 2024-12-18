from src.art_generator import ArtGenerator

def batch_generate(prompts, output_folder):
    generator = ArtGenerator()
    for idx, prompt in enumerate(prompts):
        print(f"Generating artwork for prompt: {prompt}")
        output_path = f"{output_folder}/generated_art_{idx+1}.png"
        image = generator.generate(prompt)
        image.save(output_path)
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    test_prompts = ["Abstract, bold, red tones", "Impressionism, calm, green palette"]
    batch_generate(test_prompts, "outputs")
