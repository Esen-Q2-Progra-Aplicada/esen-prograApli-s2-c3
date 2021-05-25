import requests

data = {
    "name": "shark",
    "views": 40,
    "likes": 50,
}

response = requests.put("http://127.0.0.1:5000/video/3", data=data)
print(response)
messageJson = response.json()
print(messageJson)
