import requests

response = requests.get("https://api.myip.com")
print(response.text)