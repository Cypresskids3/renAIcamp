import requests
import aicamp_day1

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Base-2407"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Why are babies so loud?",
})

import requests
import aicamp_day1

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer hf_ymarVmwrqQQaTbXBCLByEFdZMugZIKtWI"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": "What is a tree?",
})

result = aicamp_day1.make_text(output)
print(result)