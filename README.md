# 🖼️ AI Image Analyzer

An interactive web application that uses artificial intelligence to analyze and describe images in Lithuanian language.

## Features

- 📁 Upload images (PNG, JPG, JPEG, GIF, BMP, TIFF)
- 🤖 AI-powered image analysis with detailed descriptions
- 🎨 User-friendly web interface built with Streamlit
- 🔒 Local AI processing (no data sent to cloud)
- 🇱🇹 Descriptions in Lithuanian language

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Ollama gemma3:4b
- **Image Processing**: Pillow (PIL)
- **Language**: Python

## Prerequisites

- Python 3.8+
- Ollama
- gemma3:4b model

## Installation

### 1. Install Ollama

Download and install Ollama from: https://ollama.ai/

### 2. Download the AI model

```bash
ollama pull gemma3:4b
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Start Ollama server

```bash
ollama serve
```

### 2. Run the Streamlit app

```bash
streamlit run app.py
```

Or use the batch file (Windows):
```bash
paleisti.bat
```

### 3. Open your browser

Navigate to: http://localhost:8501

## How to Use

1. **Upload an image** - Click "Browse files" and select an image
2. **View the image** - Check that the image loaded correctly
3. **Analyze** - Click "🔍 Analizuoti paveikslėlį" button
4. **Get results** - Wait for the AI to provide a detailed description

## Project Structure

```
pamoka-8-github/
├── app.py                    # Main application
├── requirements.txt          # Python dependencies
├── check_ollama.py          # Ollama configuration checker
├── demo_image_creator.py    # Demo image generator
├── paleisti.bat            # Windows launcher
├── README.md               # This file
├── README_LT.md           # Lithuanian version
├── TESTAVIMAS.md          # Testing guide
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── docs/
    ├── ollama.md          # Ollama documentation
    └── streamlit.md       # Streamlit documentation
```

## Troubleshooting

### Can't connect to Ollama
```bash
# Check if Ollama is running
ollama list

# Start Ollama server
ollama serve
```

### Model not found
```bash
# Download the model
ollama pull gemma3:4b

# Check available models
ollama list
```

### Dependencies issues
```bash
# Update pip
python -m pip install --upgrade pip

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## License

This project is created for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for improvements.
