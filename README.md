# Audio-to-ChatGPT Voice Pipeline

A Python exercise from my AI and robotics training at Smart Methods (summer 2025). The script takes an audio file, transcribes it with Whisper, asks OpenAI's `gpt-3.5-turbo` for a short reply, turns the reply into speech with gTTS and plays it.

## How it works

1. Whisper's `base` model transcribes the audio locally. The model weights download the first time it runs.
2. The transcript is sent to the OpenAI Chat Completions API with a system prompt that asks for a short answer.
3. gTTS sends the reply to Google's text-to-speech service and saves the audio as `output.mp3`.
4. pydub plays `output.mp3`.

Steps 2 and 3 need an internet connection. The transcript and the reply are also printed in the terminal.

## Setup

Use Python 3.11 or 3.12. pydub relies on the `audioop` module, which was removed in Python 3.13.

```sh
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install openai openai-whisper gTTS pydub
```

The Whisper package is called `openai-whisper` on PyPI and is imported as `whisper`.

Install [FFmpeg](https://ffmpeg.org/download.html) and make sure `ffmpeg` and `ffplay` are on your `PATH`. Whisper uses FFmpeg to read the audio, and pydub uses it to decode and play the MP3. On Ubuntu, run `sudo apt install ffmpeg`; on macOS, run `brew install ffmpeg`.

Set your OpenAI API key in the terminal you will run the script from, and never commit it:

```sh
export OPENAI_API_KEY="your-api-key"      # macOS or Linux
$env:OPENAI_API_KEY = "your-api-key"      # Windows PowerShell
```

The script reads the key from the environment; it does not load a `.env` file. Requests are billed to your OpenAI account, and the account needs access to `gpt-3.5-turbo`.

## Usage

Run from the repository root:

```sh
python Main.py                    # uses the included audio.wav
python Main.py path/to/file.wav   # uses another audio file
```

The script works on a recorded file. It does not listen to a microphone or keep a conversation history. `output.mp3` is written to the current folder and replaced on every run.

## Files

- [`Main.py`](Main.py): the whole pipeline.
- [`audio.wav`](audio.wav): sample input.
- `output.mp3`: generated speech, not committed.

## Limitations

- If a step fails, the script prints the error and stops. It does not retry, and the exit code is still 0.
- gTTS speaks English by default, whatever language the input was in.
- After a failed run, the `output.mp3` from an earlier run stays in place.
