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


speech_file_path = Path(__file__).parent / "speech.mp3"

response = openai_client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)
