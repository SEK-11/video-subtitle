# Video Clip Generator

Automatically create engaging short video clips from long-form content with AI-powered transcription, scoring, and subtitle generation.

## Features

- Upload video files (podcasts, interviews, etc.)
- AI transcription using Whisper
- Intelligent segment scoring for viral potential
- Automatic subtitle generation with emojis
- Export social media-ready clips

## Quick Start

### Using Docker
```bash
docker-compose up --build
```

### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Install FFmpeg (required for video processing)
# Ubuntu/Debian: sudo apt install ffmpeg
# macOS: brew install ffmpeg

# Run the server
cd backend && python app.py
```

## API Usage

### Upload Video
```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_video.mp4"
```

### Check Status
```bash
curl "http://localhost:8000/status/{job_id}"
```

## Output

The system generates:
- Transcribed segments with timestamps
- Engagement scores for each segment
- 3 short video clips with animated subtitles and emojis
- Clips optimized for social media (vertical format recommended)