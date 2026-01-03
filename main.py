#!/usr/bin/env python3
"""
YouTube Auto Dub - Day 05
Enhanced with translation and TTS functionality
"""

import sys
import os
from pathlib import Path

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from core_utils import setup_directories, validate_url, get_video_id, Config
    from youtube import YouTubeDownloader
    from media import AudioProcessor, VideoProcessor
    from engines import TranslationEngine, TTSEngine, STTEngine, DiarizationEngine
except ImportError as e:
    print(f"Error: {e}")
    sys.exit(1)

def main():
    print("YouTube Auto Dub - Starting...")
    
    # Setup directories
    setup_directories()
    
    # TODO: Get YouTube URL from user
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Placeholder
    
    # Validate URL
    if not validate_url(youtube_url):
        print("Invalid URL!")
        return
    
    print(f"Processing URL: {youtube_url}")
    
    # Initialize YouTube downloader
    downloader = YouTubeDownloader()
    
    # Get video info
    video_info = downloader.get_video_info(youtube_url)
    if video_info:
        print(f"Video found: {video_info.get('title', 'Unknown')}")
        print(f"Duration: {video_info.get('duration', 0)} seconds")
    else:
        print("Failed to get video info!")
        return
    
    # Download audio
    audio_file = downloader.download_audio(youtube_url)
    if audio_file and Path(audio_file).exists():
        print(f"Audio downloaded: {audio_file}")
        
        # Process audio
        audio_processor = AudioProcessor()
        processed_audio = audio_processor.extract_audio(audio_file)
        if processed_audio:
            print(f"Audio processed: {processed_audio}")
            
            # Transcribe audio
            stt_engine = STTEngine()
            transcription = stt_engine.transcribe(processed_audio, language='en')
            print(f"Transcription: {transcription}")
            
            # Translate text
            translator = TranslationEngine()
            translated_text = translator.translate(transcription, 'es')
            print(f"Translation: {translated_text}")
            
            # Synthesize speech
            tts_engine = TTSEngine()
            tts_audio = tts_engine.synthesize(translated_text, 'es', voice='female')
            print(f"TTS audio: {tts_audio}")
        else:
            print("Failed to process audio!")
    else:
        print("Failed to download audio!")
        return
    
    # TODO: Implement video reconstruction
    print("YouTube Auto Dub - Finished!")

if __name__ == "__main__":
    main()
