import requests

BASE = "http://127.0.0.1:5000/"


data = [
    {"likes": 11, "name": "Praveen", "views": 69},
    {"likes": 12, "name": "Pveen", "views": 693},
    {"likes": 33, "name": "Prav", "views": 698},
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())
