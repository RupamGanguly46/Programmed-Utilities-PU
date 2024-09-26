from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def setup_ffmpeg_path():
    ffmpeg_path = 'C:/ffmpeg/bin'  # Adjust this to your ffmpeg path
    if ffmpeg_path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + ffmpeg_path

def generate_speech(text, filename="speech.mp3"):
    # Generate speech from text
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Speech saved as {filename}")
    return filename


def mix_with_background(speech_file, background_file, output_file):
    # Load the speech and background music files
    speech = AudioSegment.from_file(speech_file)
    background = AudioSegment.from_file(background_file)

    # Repeat the speech to match the length of the background music
    speech = speech * int(background.duration_seconds // speech.duration_seconds)

    # Mix speech and background music
    combined = background.overlay(speech)

    # Export the final audio as an MP3 file
    combined.export(output_file, format="mp3")
    print(f"Ringtone saved as {output_file}")


def create_custom_ringtone(caller_name, background_file, output_folder="ringtones"):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Generate speech text
    text = f"Incoming call ! {caller_name}. " * 5

    # Generate speech MP3
    speech_file = f"{output_folder}/speech_{caller_name}.mp3"
    generate_speech(text, speech_file)

    # Create the final ringtone
    output_file = f"{output_folder}/{caller_name}_ringtone.mp3"
    mix_with_background(speech_file, background_file, output_file)

    # Clean up temporary speech file
    os.remove(speech_file)
    return output_file


if __name__ == "__main__":
    # Example usage:
    setup_ffmpeg_path()
    contacts = ["Shubhang Dixit", "Sanskar Khandelwal", "Ritee", "Srikant Choubey", "Anupam Paul"]
    background_music = "radiate.mp3"  # Path to your background music file

    for contact in contacts:
        ringtone = create_custom_ringtone(contact, background_music)
        print(f"Generated ringtone for {contact}: {ringtone}")
