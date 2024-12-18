# Lee AI Art Generator 🎨  

Lee AI is an AI-powered Python project that generates art portraits based on user-defined prompts.  
It uses Generative Adversarial Networks (GANs) and Neural Style Transfer for seamless, high-quality artwork.  

## Features  
- Customizable prompts for art generation  
- Supports multiple styles (realism, abstract, impressionism)  
- Fast inference using pre-trained models  

## Core Components  
1. **Prompt Parser**: Analyzes input prompts to extract styles, moods, and color preferences.  
2. **Color Palette Generator**: Generates color schemes based on user-defined prompts.  
3. **Image Renderer**: Renders digital artwork based on parsed prompts and palettes.  
4. **AI Model Loader**: Loads pre-trained GAN models for advanced art generation.  

## Workflow  
1. **Input**: User provides a prompt (e.g., "Abstract, calm mood, blue and yellow").  
2. **Processing**:  
   - Parse the prompt.  
   - Generate a color palette.  
   - Render the image or enhance it using a model.  
3. **Output**: Final artwork is saved and displayed for the user.  

## Technologies Used  
- Python  
- PyTorch  
- Pillow  
- Matplotlib  
- Flask  
