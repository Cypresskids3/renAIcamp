import requests
import aicamp_day1

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Do you think turtles should be pets?",
})

result = aicamp_day1. make_text(output)
print(result)

