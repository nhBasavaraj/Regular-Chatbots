import requests

url = 'https://api.jina.ai/v1/embeddings'

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer JINA_API_KEY'
}

data = {
  'input': ["python"],
  'model': 'jina-embeddings-v2-base-en'
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
