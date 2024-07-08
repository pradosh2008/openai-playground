import os
from dotenv import load_dotenv  # Used to load environment variables from a .env file
from openai import OpenAI
import time

# Load environment variables from .env file
load_dotenv()
# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



openai_client = OpenAI(
    api_key = OPENAI_API_KEY,
    organization ='org-zy91VcIKogamLudMARObBJbb'
)

stream = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "what do you think about india"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")


