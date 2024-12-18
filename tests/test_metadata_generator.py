import unittest
import os
from tools.metadata_generator import generate_metadata

class TestMetadataGenerator(unittest.TestCase):
    def test_generate_metadata(self):
        prompt = "Abstract, bold, blue and yellow"
        output_path = "outputs/test_art.png"
        metadata_path = output_path.replace(".png", ".json")
        
        generate_metadata(prompt, output_path)
        self.assertTrue(os.path.exists(metadata_path))  # Check if metadata file is created
        
        # Clean up
        if os.path.exists(metadata_path):
            os.remove(metadata_path)

if __name__ == '__main__':
    unittest.main()
