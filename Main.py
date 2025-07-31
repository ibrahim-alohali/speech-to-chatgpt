import os
import sys
import openai
import whisper
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pydub.exceptions import CouldntDecodeError

def main():
    # Get input filename from command-line argument or default to "audio.wav"
    input_audio = sys.argv[1] if len(sys.argv) > 1 else "audio.wav"

    # Load Whisper model once
    try:
        model = whisper.load_model("base")
    except Exception as e:
        print(f"Error loading Whisper model: {e}")
        return

    # Step 1: Transcribe audio file
    try:
        result = model.transcribe(input_audio)
        transcribed_text = result["text"]
        print("Transcribed Text:")
        print(transcribed_text)
    except FileNotFoundError:
        print(f"Audio file '{input_audio}' not found. Please provide a valid file.")
        return
    except Exception as e:
        print(f"Error during transcription: {e}")
        return

    # Step 2: Get response from OpenAI GPT
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Reply in a short sentence while providing enough response and reasoning to satisfy the user."},
                {"role": "user", "content": transcribed_text}
            ]
        )
        gpt_response = response.choices[0].message.content
        print("\nGPT Response:")
        print(gpt_response)
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        return

    # Step 3: Generate speech from GPT response and save to output.mp3
    try:
        tts = gTTS(gpt_response)
        tts.save("output.mp3")
        print("\nSaved output.mp3")
    except Exception as e:
        print(f"Error generating speech with gTTS: {e}")
        return

    # Step 4: Play the output audio file using pydub
    try:
        audio = AudioSegment.from_file("output.mp3")
        print("Playing output.mp3...")
        play(audio)
    except CouldntDecodeError:
        print("Warning: Could not play audio. Please ensure you have the necessary audio playback dependencies installed (e.g., ffmpeg or avlib).")
    except Exception as e:
        print(f"Error during audio playback: {e}")

if __name__ == "__main__":
    main()
