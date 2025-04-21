# 3.​ Write a script that sends an HTTP request to example.com and prints the response
import requests

res = requests.get("https://example.com")
print(res.headers)