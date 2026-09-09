# Audio-to-ChatGPT Voice Pipeline

A Python training project that transcribes an audio file, requests a short text response, converts it to speech, and plays the result. The original implementation uses Whisper's `base` model, OpenAI's `gpt-3.5-turbo` model, gTTS, and pydub.

## How it works

1. Whisper loads the `base` model and transcribes the input file locally. The model weights may need to download on first use.
2. The script sends the transcript to the OpenAI API using `OPENAI_API_KEY`.
3. gTTS sends the generated response text to Google Translate's text-to-speech service and saves the returned audio as `output.mp3`.
4. pydub decodes and plays that MP3 locally.

Both the OpenAI request and speech synthesis require network access. gTTS is an interface to a remote service, as described in the [gTTS documentation](https://gtts.readthedocs.io/en/latest/). The transcript and generated response are also printed in the terminal.

## Setup

Use a Python environment compatible with the dependencies; Python 3.11 is a reasonable starting point for this older script. The repository does not contain a lockfile or a newly tested environment.

Create and activate a virtual environment from the repository root:

```sh
python -m venv .venv
```

```sh
# macOS or Linux
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

Install the packages imported by the script:

```sh
python -m pip install openai openai-whisper gTTS pydub
```

The package name is `openai-whisper`, while its Python import is `whisper`. See the [official Whisper setup instructions](https://github.com/openai/whisper#setup).

Install FFmpeg and ensure `ffmpeg` and `ffplay` are available on `PATH`. Whisper requires FFmpeg to decode audio; pydub uses it for MP3 decoding and can use `ffplay` for playback. See [pydub's installation and playback guidance](https://github.com/jiaaro/pydub#installation).

```sh
# Ubuntu or Debian
sudo apt update
sudo apt install ffmpeg
```

```sh
# macOS with Homebrew
brew install ffmpeg
```

For Windows, use a Windows build linked from the [FFmpeg download page](https://ffmpeg.org/download.html) and add its `bin` directory to `PATH`. An available audio output device is needed for playback.

Set the API key in the same terminal that will run the script. Replace `your-api-key` with your own key; never commit it:

```sh
# macOS or Linux
export OPENAI_API_KEY="your-api-key"
```

```powershell
# Windows PowerShell
$env:OPENAI_API_KEY = "your-api-key"
```

```bat
:: Windows Command Prompt
set "OPENAI_API_KEY=your-api-key"
```

The code reads the process environment directly; it does not load a `.env` file. The OpenAI request needs API access to the configured model and may incur usage charges. The original model choice is retained; account access and current service availability have not been tested during this cleanup.

## Usage and output

Run from the repository root:

```sh
python Main.py
python Main.py "path/to/myfile.wav"
```

The first command uses the included [`audio.wav`](audio.wav). The second accepts a different input path. This is file-based input; the script does not record a microphone or maintain a conversation history.

The terminal displays the transcript, response, and progress or error messages. A successful speech-synthesis step writes `output.mp3` in the current working directory, overwriting any previous file with that name. Playback failure can still leave the generated MP3 available.

## Files and limitations

- [`Main.py`](Main.py): the complete pipeline.
- [`audio.wav`](audio.wav): original sample audio.
- `output.mp3`: generated speech, excluded from version control.

The script catches errors at model loading, transcription, API, synthesis, and playback stages. It reports them as text; it does not implement retries or reliable failure exit codes. Speech synthesis uses gTTS's default English language, regardless of the detected input language. A failed run can leave an older `output.mp3` in place.

Use audio you are comfortable processing through the described services. Keep API keys and private recordings out of commits. Documentation was reviewed against the source and upstream setup guidance; no dependencies were installed, audio processed, paid API calls made, or historical tests rerun during this cleanup.
