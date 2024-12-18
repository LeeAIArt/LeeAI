import unittest
from src.ai_model_loader import AIModelLoader

class TestAIModelLoader(unittest.TestCase):
    def test_load_model(self):
        model_loader = AIModelLoader("models/pretrained_model.pth")
        model = model_loader.load_model()
        self.assertIsNotNone(model)  # Ensure model is loaded
        self.assertTrue(callable(model))  # Check if the model is callable

    def test_predict_without_loading(self):
        model_loader = AIModelLoader("models/pretrained_model.pth")
        with self.assertRaises(ValueError):
            model_loader.predict(None)  # Should raise an error if model is not loaded

if __name__ == '__main__':
    unittest.main()
