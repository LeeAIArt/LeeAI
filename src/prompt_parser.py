import re

class PromptParser:
    def __init__(self, prompt):
        self.prompt = prompt.lower()
        self.styles = ["abstract", "realism", "impressionism", "surrealism", "modern", "sketch"]
        self.moods = ["vibrant", "dark", "calm", "energetic", "dreamlike"]
        self.colors = ["red", "blue", "green", "yellow", "orange", "black", "white"]

    def parse(self):
        style = self._extract(self.styles, "style")
        mood = self._extract(self.moods, "mood")
        color_palette = self._extract(self.colors, "colors")
        return {"style": style, "mood": mood, "colors": color_palette}

    def _extract(self, keywords, category):
        matches = [kw for kw in keywords if kw in self.prompt]
        return matches[0] if matches else f"default_{category}"

if __name__ == "__main__":
    # Example Usage
    prompt = "Abstract, calm mood with blue and yellow tones"
    parser = PromptParser(prompt)
    parsed = parser.parse()
    print(parsed)  # Output: {'style': 'abstract', 'mood': 'calm', 'colors': 'blue'}
