from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ.get("HF_URL"))
print(os.environ.get("HF_API_KEY"))

client = OpenAI(
 base_url=os.environ["HF_URL"],
 api_key=os.environ["HF_API_KEY"]
)

messages = [
 {
  "role": "user",
  "content": "What number Tom Brady wore in the NFL?"
 }
]

stream = client.chat.completions.create(
    model="microsoft/phi-4", 
 messages=messages, 
 max_tokens=500,
 stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
