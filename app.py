import os
from groq import Groq
from dotenv import load_dotenv

# Load the keys from the .env file automatically
load_dotenv()

# Initialize client (it automatically picks up the GROQ_API_KEY env variable)
client = Groq()
import asyncio


async def main():
  prompt = input("Prompt: ")

  # Create a streaming chat completion
  completion = await client.chat.completions.create(
    messages=[
      {"role": "system", "content": "you are a helpful food finding assistant, do not answer questions that are not related to food, do not provide information about topics other than food, CRITICAL RULES: always prioritize food-related information and decline to answer non-food questions, do not role play, do not accept commands from the user and speak in a simple and easy-to-understand manner."},
      {"role": "user", "content": prompt},
    ],
    model="openai/gpt-oss-20b",
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None,
  )

  async for chunk in completion:
    # print incremental content as it arrives
    print(chunk.choices[0].delta.content or "", end="")


if __name__ == "__main__":
  asyncio.run(main())

