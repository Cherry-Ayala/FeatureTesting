import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

api_key = os.getenv("DS_API_KEY", '')
if not api_key:
  raise Exception("A key should be provided to invoke the endpoint")

client = ChatCompletionsClient(
    endpoint='https://DeepSeek-R1-stk.eastus2.models.ai.azure.com',
    credential=AzureKeyCredential(api_key)
)

model_info = client.get_model_info()
print("Model name:", model_info.model_name)
print("Model type:", model_info.model_type)
print("Model provider name:", model_info.model_provider_name)
payload = {
  "messages": [
    {
      "role": "system",
      "content": "You're a helpful assistant"
    },
    {
      "role": "user",
      "content": "Build a python function that divided two numbers"
    },
  ],
}
response = client.complete(payload)
print("Response:", response.choices[0].message.content)
print("Model:", response.model)
print("Usage:")
print(" Prompt tokens:", response.usage.prompt_tokens)
print(" Total tokens:", response.usage.total_tokens)
print(" Completion tokens:", response.usage.completion_tokens)