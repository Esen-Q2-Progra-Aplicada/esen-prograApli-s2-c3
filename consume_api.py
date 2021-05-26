import requests

data = {
    "name": "sharkx",
    "views": 401,
    "likes": 501,
}

""" response = requests.get("http://127.0.0.1:5000/video/4")
response = requests.put("http://127.0.0.1:5000/video/1", data=data) """
response = requests.patch("http://127.0.0.1:5000/video/7", data=data)
""" response = requests.delete("http://127.0.0.1:5000/video/6") """
print(response)
messageJson = response.json()
print(messageJson)
