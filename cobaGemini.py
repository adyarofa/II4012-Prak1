
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Simple Gemini Chat")
print("Type 'exit' to quit.\n")

history = []

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye.")
        break
    if not user_input:
        continue

    history.append(f"User: {user_input}")
    prompt = "\n".join(history) + "\nAssistant:"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        bot_reply = (response.text or "").strip()
        print(f"Bot: {bot_reply}\n")
        history.append(f"Assistant: {bot_reply}")
    except Exception as e:
        print(f"Error: {e}\n")