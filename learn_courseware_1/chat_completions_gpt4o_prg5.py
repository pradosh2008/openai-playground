from openai import OpenAI
from dotenv import load_dotenv
import os 

# Load environment variables from .env file
load_dotenv()
# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = OPENAI_API_KEY,
    organization ='org-zy91VcIKogamLudMARObBJbb'
)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
