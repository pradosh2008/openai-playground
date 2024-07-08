from dotenv import load_dotenv  # Used to load environment variables from a .env file
from openai import OpenAI
import time
import os
from pathlib import Path
import warnings

# Load environment variables from .env file
load_dotenv()
# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


openai_client = OpenAI(
    api_key = OPENAI_API_KEY,
    organization ='org-zy91VcIKogamLudMARObBJbb'
)

audio_file_path = Path(__file__).parent / "speech.mp3"

audio_file = open(audio_file_path, "rb")

transcript = openai_client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcript.text)



translated_response = openai_client.audio.translations.create(
  model="whisper-1",
  file=audio_file
)

# Check the type and content of the response
print(f"Type of response: {type(translated_response)}")
print(f"Response content: {translated_response}")

print(translated_response.text)