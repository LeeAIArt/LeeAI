import json
from datetime import datetime

def generate_metadata(prompt, output_path):
    metadata = {
        "prompt": prompt,
        "timestamp": datetime.now().isoformat(),
        "output_file": output_path
    }
    with open(output_path.replace(".png", ".json"), "w") as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata saved alongside {output_path}")

if __name__ == "__main__":
    generate_metadata("Abstract, bold, blue and yellow", "outputs/generated_art_1.png")
