import requests

url = "https://reqres.in/api/users/659"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)