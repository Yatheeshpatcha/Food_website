import os
from groq import Groq
from dotenv import load_dotenv

# Load the keys from the .env file automatically
load_dotenv()

# Initialize client (it automatically picks up the GROQ_API_KEY env variable)
client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": "what is the price of suchi\n"
      },
      {
        "role": "assistant",
        "content": "I’m not able to give you a current, location‑specific price for sushi, since that information can change frequently and varies a lot depending on where you are, the type of restaurant, and the specific items you order.  \n\nHowever, I can share some general price ranges you’ll often see:\n\n| Type of sushi | Typical price range (U.S.) |\n|---------------|----------------------------|\n| **Conveyor‑belt (kaiten) sushi** | $1–$3 per piece (often $10–$20 for a full plate) |\n| **Fast‑casual sushi bowls or rolls** | $5–$12 per item |\n| **Mid‑range sit‑down sushi restaurant** | $2–$5 per piece for basic nigiri; $8–$15 for specialty rolls |\n| **High‑end omakase or premium sushi** | $30–$150+ per person, depending on the chef and fish quality |\n\nThese are just ballpark figures; actual prices can be higher in major metropolitan areas, near waterfronts, or at specialty sushi bars that use premium ingredients like toro, uni, or imported fish.  \n\n**Tips for finding the most accurate price:**\n\n1. **Check the restaurant’s website or menu** – many places post up‑to‑date pricing online.\n2. **Use food‑delivery apps** (DoorDash, Uber Eats, Grubhub, etc.) – they show current menu prices for local spots.\n3. **Call the establishment** – a quick phone call can confirm today’s specials or any seasonal pricing.\n4. **Look at recent reviews** on sites like Yelp or TripAdvisor – diners often mention whether a place is “budget‑friendly,” “mid‑range,” or “pricey.”\n\nIf you let me know a specific city or type of sushi you’re interested in, I can offer more tailored guidance on what to expect and how to locate the best‑priced options in that area."
      },
      {
        "role": "user",
        "content": "how much is it to buy in bulk\n\n"
      }
    ],
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

