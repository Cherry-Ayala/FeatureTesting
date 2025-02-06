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

prompt = """
def process_text(input_text):
    if input_text:
        result = []
        for line in input_text.split('\n'):
            if line.startswith('#'):
                if len(line) > 5:
                    result.append(line.strip().upper())
                else:
                    result.append("SHORT_HEADER")
            else:
                if "TODO" in line:
                    result.append(f"TODO: {line.strip()}")
                else:
                    words = line.split()
                    if len(words) > 10:
                        result.append("LONG_LINE")
                    else:
                        result.append(' '.join(w[::-1] for w in words))
        return '\n'.join(result)
    else:
        return "EMPTY_INPUT"""

model_info = client.get_model_info()
print("Model name:", model_info.model_name)
print("Model type:", model_info.model_type)
print("Model provider name:", model_info.model_provider_name)
payload = {
  "messages": [
    {
      "role": "system",
      "content": "Based on this code tell me which refactoring patterns should be useful, be sure to put them at the start of the response"
    },
    {
      "role": "user",
      "content": prompt
    },
    {
      "role": "system",
      "content": "For the final response, respond with the code block, denoted by ```, and its according documentation string for the created functions within it. If you can, apply the appropriate type hints for the function and the documentation as well, and always include the programming language used at the beginning of the code-block."
    },
    {
      "role": "system",
      "content": "Lastly, also return the patterns used for the generation of this code, this should be at the start of the response."
    },
  ],
}
response = client.complete(payload)
print("Response:", response.choices[0].message.content)
print("Model:", response.model)
print("Payload")
print(payload)
print("Usage:")
print(" Prompt tokens:", response.usage.prompt_tokens)
print(" Total tokens:", response.usage.total_tokens)
print(" Completion tokens:", response.usage.completion_tokens)