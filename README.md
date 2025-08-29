# 🎬 AI Video Subtitle Generator

Automatically add animated subtitles to any video using AI-powered speech recognition. Perfect for creating engaging social media content, podcasts, interviews, and educational videos.

## ✨ Features

- 🎯 **AI Transcription**: Uses OpenAI Whisper for accurate speech-to-text
- 📝 **Smart Chunking**: Displays 4-5 words at a time for better readability
- 🎨 **Animated Subtitles**: Floating text with scaling animations
- 🎪 **Professional Styling**: White text with black background for clarity
- 🚀 **Easy to Use**: Single command to process any video
- 📱 **Social Media Ready**: Optimized subtitle positioning and sizing

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- FFmpeg

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd video-subtitle-generator
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**
   ```bash
   # Ubuntu/Debian
   sudo apt install ffmpeg
   
   # macOS
   brew install ffmpeg
   
   # Windows
   # Download from https://ffmpeg.org/download.html
   ```

## 🚀 Usage

### Basic Usage
```bash
# Activate virtual environment
source venv/bin/activate

# Add subtitles to your video
python3 simple_subtitles.py "path/to/your/video.mp4"
```

### Example
```bash
python3 simple_subtitles.py "my_podcast.mp4"
```

Output: `subtitled_video.mp4` with animated subtitles

## 🎥 How It Works

1. **Audio Extraction**: Extracts audio from your video
2. **AI Transcription**: Uses Whisper AI to convert speech to text
3. **Text Processing**: Cleans and chunks text into 4-5 word segments
4. **Animation Generation**: Creates floating, scaling text animations
5. **Video Rendering**: Overlays subtitles onto original video with FFmpeg

## ⚙️ Configuration

### Whisper Model Options
Edit `simple_subtitles.py` line 27 to change accuracy vs speed:

```python
# Options: "tiny", "base", "small", "medium", "large"
model = whisper.load_model("small")  # Current setting
```

- `tiny` - Fastest, least accurate
- `base` - Good balance
- `small` - Better accuracy (recommended)
- `medium` - High accuracy, slower
- `large` - Best accuracy, slowest

### Customization Options

You can modify these parameters in the code:

- **Font Size**: Change `fontsize=50` (line 52)
- **Animation Speed**: Modify `sin(2*PI*(t-{chunk_start})*0.8)` (line 49)
- **Text Position**: Adjust `y=h-120` (line 52)
- **Words per Chunk**: Change `words_per_chunk=4` (line 37)

## 📁 Project Structure

```
video-subtitle-generator/
├── simple_subtitles.py    # Main script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── venv/                 # Virtual environment
└── subtitled_video.mp4   # Output file
```

## 🎨 Output Features

- **Animated Text**: Gentle floating and scaling effects
- **Smart Timing**: Each word chunk appears for appropriate duration
- **Professional Look**: White text with black background box
- **Responsive Design**: Text stays within video frame boundaries
- **High Quality**: Preserves original video and audio quality

## 🔧 Troubleshooting

### Common Issues

**"FFmpeg not found"**
```bash
# Make sure FFmpeg is installed and in PATH
ffmpeg -version
```

**"No module named 'whisper'"**
```bash
# Make sure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**"Text going outside frame"**
- Reduce font size in the code
- Use shorter word chunks
- Adjust text positioning

**"Poor transcription quality"**
- Use a larger Whisper model ("medium" or "large")
- Ensure good audio quality in source video
- Check for background noise

## 📋 Requirements

- Python 3.8+
- FFmpeg
- ~2GB RAM for "small" Whisper model
- ~5GB RAM for "large" Whisper model

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - feel free to use for personal and commercial projects.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for speech recognition
- [FFmpeg](https://ffmpeg.org/) for video processing
- Inspired by tools like Submagic and similar subtitle generators

---

**Made with ❤️ for content creators**