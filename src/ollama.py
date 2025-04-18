from openai import OpenAI
import os

client = OpenAI(
    base_url = os.getenv("OLLAMA_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"), # required, but unused
)

response = client.chat.completions.create(
  model=os.getenv("OLLAMA_MODEL"),
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France"},
  ]
)
print(response.choices[0].message.content)