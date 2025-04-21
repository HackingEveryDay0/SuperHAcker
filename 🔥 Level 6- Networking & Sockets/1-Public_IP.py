#1.​ Fetch and print your public IP address using an API.

import requests

with requests.get("https://api.ipify.org?format=json") as res:
    print("My public IP Address: ", res.json()["ip"])