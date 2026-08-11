import os
from groq import Groq
from dotenv import load_dotenv

# Load the keys from the .env file automatically
load_dotenv()

# Initialize client (it automatically picks up the GROQ_API_KEY env variable)
client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is the capital of France?",
            "token_limit": 1000
        }
    ],
    model="openai/gpt-oss-20b",
    # Make sure stream=True is NOT here
)

# This will now work without errors
print(chat_completion.choices[0].message.content)


