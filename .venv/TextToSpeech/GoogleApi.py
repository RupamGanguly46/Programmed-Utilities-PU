from gtts import gTTS
import os

def text_to_speech(text, filename='output.mp3'):
    # Initialize gTTS with the text and language (e.g., 'en' for English)
    tts = gTTS(text=text, lang='en')

    # Save the speech to an MP3 file
    tts.save(filename)
    print(f"MP3 file saved as: {filename}")

if __name__ == "__main__":
    # Example text to convert to speech
    text = f"Incoming Call ! {ContactName}"

    # Define the filename for the MP3 file
    filename = "notification.mp3"

    # Call the text_to_speech function to generate the MP3 file
    text_to_speech(text, filename)

    # Optionally, play the MP3 file (works on some platforms)
    if os.name == 'nt':
        os.startfile(filename)
    elif os.name == 'posix':
        os.system(f"mpg123 {filename}")
