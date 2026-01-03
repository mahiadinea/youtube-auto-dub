# YouTube Auto Dub - Day 05

## Project Overview
YouTube Auto Dub is a tool to automatically dub YouTube videos into different languages.

## Features (Planned)
- YouTube video downloading
- Audio extraction and processing
- Speech-to-text transcription
- Text translation
- Voice synthesis
- Audio mixing and video reconstruction

## Current Status
Day 05: Enhanced with translation and TTS functionality.

## New Features
- **Translation Engine**: Basic Google Translate integration with language detection
- **TTS Engine**: Edge TTS integration with multi-language voice support
- **Enhanced Audio Processing**: Audio chunking for better processing
- **Video Processing**: Audio-video merging capabilities
- **Better Error Handling**: Custom exceptions for all engine types
- **Language Support**: 10 languages with male/female voice options

## Key Components
- `engines.py`: Real translation and TTS implementations
- `media.py`: Enhanced audio/video processing with chunking
- `core_utils.py`: Added language and voice configuration
- `main.py`: Complete workflow integration

## Supported Languages
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
- Vietnamese (vi)

## Installation
```bash
pip install -r requirements.txt
```

**Note**: Requires FFmpeg to be installed and available in PATH.

## Usage
```bash
python main.py
```

## Dependencies
- yt-dlp: YouTube video downloading
- requests: HTTP requests and translation API
- edge-tts: Text-to-speech synthesis
- numpy: Array processing
- librosa: Audio analysis
- ffmpeg-python: FFmpeg Python bindings

## Next Steps
- Implement actual speech-to-text with Faster-Whisper
- Add real speaker diarization with Pyannote
- Implement audio separation with Demucs
- Add video reconstruction pipeline
- Improve translation quality and add more languages
