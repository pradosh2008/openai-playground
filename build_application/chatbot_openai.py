import os
from dotenv import load_dotenv  # Used to load environment variables from a .env file
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(
    api_key=OPENAI_API_KEY,
    organization ='org-zy91VcIKogamLudMARObBJbb'
)


def get_response(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = get_response(user_input)
    print(f"Bot: {response}")
