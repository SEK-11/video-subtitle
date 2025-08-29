#!/usr/bin/env python3
import sys
import whisper
import subprocess
import re

def clean_text(text):
    """Clean text for ffmpeg drawtext filter"""
    # Remove special characters that break ffmpeg
    text = re.sub(r"[':\"\\]", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    return text.strip()

def split_into_chunks(text, words_per_chunk=4):
    """Split text into chunks of 4-5 words"""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), words_per_chunk):
        chunk = ' '.join(words[i:i + words_per_chunk])
        chunks.append(chunk)
    
    return chunks

def add_subtitles(video_path: str):
    print("Transcribing...")
    model = whisper.load_model("small")
    result = model.transcribe(video_path)
    
    print("Adding subtitles (4-5 words at a time)...")
    
    # Create drawtext filters for each segment
    filters = []
    for segment in result["segments"]:
        text = clean_text(segment["text"])
        if not text:
            continue
            
        # Split into 4-5 word chunks
        chunks = split_into_chunks(text, 4)
        
        start = segment["start"]
        end = segment["end"]
        duration = end - start
        chunk_duration = duration / len(chunks) if chunks else duration
        
        # Create filter for each chunk
        for i, chunk in enumerate(chunks):
            chunk_start = start + (i * chunk_duration)
            chunk_end = start + ((i + 1) * chunk_duration)
            
            # Floating animation - keep within frame
            float_y = f"h-120+5*sin(2*PI*(t-{chunk_start})*0.8)"
            scale_anim = f"1+0.05*sin(2*PI*(t-{chunk_start})*2)"
            
            # Show chunk with animation - smaller font to fit
            filter_text = f"drawtext=text='{chunk}':fontsize=50*{scale_anim}:fontcolor=white:x=(w-text_w)/2:y={float_y}:box=1:boxcolor=black@0.8:boxborderw=3:enable='between(t,{chunk_start},{chunk_end})'"
            filters.append(filter_text)
    
    # Combine all filters
    vf = ",".join(filters) if filters else "null"
    
    output_path = "subtitled_video.mp4"
    
    cmd = [
        'ffmpeg', '-y',
        '-i', video_path,
        '-vf', vf,
        '-c:a', 'copy',
        output_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Success! Output: {output_path}")
    else:
        print(f"❌ Error: {result.stderr}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python simple_subtitles.py <video_file>")
        sys.exit(1)
    add_subtitles(sys.argv[1])