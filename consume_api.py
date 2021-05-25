import requests

response = requests.get("http://127.0.0.1:5000/video/0")
print(response)
messageJson = response.json()
print(messageJson)
