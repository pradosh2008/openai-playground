import os
from dotenv import load_dotenv  # Used to load environment variables from a .env file
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


openai_client = OpenAI(
    api_key = OPENAI_API_KEY,
    organization ='org-zy91VcIKogamLudMARObBJbb'
)

response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "How old are you?"}]
)

# print(response)
# Print the response contents
print(response.choices[0].message.content)