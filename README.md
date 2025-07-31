# Audio-to-ChatGPT Voice Pipeline

This project demonstrates an end-to-end pipeline:
- Speech-to-text with [OpenAI Whisper](https://github.com/openai/whisper)
- Querying [OpenAI GPT-3.5 Turbo](https://platform.openai.com/docs/guides/gpt)
- Converting response to speech with [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/)
- Playing the AI-generated response out loud

---

## Features

- Audio file transcription using Whisper (STT)
- Short, conversational AI responses (via ChatGPT/GPT-3.5 Turbo)
- Text-to-speech synthesis of the response (gTTS)
- Automatic playback of AI response
- Error handling for missing files, failed API calls, and audio playback
- Specify any audio file as input (default: `audio.wav`)

---

## Setup

1. **Clone the repository** and place your audio file (e.g., `audio.wav`) in the project folder.

2. **Install dependencies:**
   ```bash
   pip install openai whisper gtts pydub

You may also need ffmpeg for audio playback (required by pydub).

On Mac/Linux:

brew install ffmpeg

On Windows: Download from ffmpeg.org
	3.	Set your OpenAI API key:
	•	Create a free or paid account at https://platform.openai.com/
	•	Get your API key from your account dashboard.
	•	Set it as an environment variable before running the script:

export OPENAI_API_KEY=sk-...   # Linux/Mac
set OPENAI_API_KEY=sk-...      # Windows CMD
$env:OPENAI_API_KEY="sk-..."   # Windows PowerShell



⸻

Usage

Run the script with your audio file:

python Main.py              # uses audio.wav by default
python Main.py myfile.wav   # specify another file


⸻

Sample Audio

A short sample (audio.wav) is included for demo/testing purposes.

⸻

Notes
	•	All processing is local except for the GPT response (uses your OpenAI API key—do not share this key!).
	•	The pipeline will gracefully report errors if any stage fails.

⸻

Project Structure

-Main.py
-audio.wav
-output.mp3 (created automatically)

-README.md


⸻

Security Notice:
Do not share your API key or commit it to public repos.

