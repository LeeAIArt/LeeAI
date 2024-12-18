import unittest
import os
from tools.batch_generator import batch_generate

class TestBatchGenerator(unittest.TestCase):
    def test_batch_generate(self):
        prompts = ["Abstract, bold, red tones", "Impressionism, calm, green palette"]
        output_folder = "outputs"
        batch_generate(prompts, output_folder)

        # Check if files are created
        for idx, _ in enumerate(prompts):
            output_file = f"{output_folder}/generated_art_{idx+1}.png"
            self.assertTrue(os.path.exists(output_file))
            # Clean up
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
