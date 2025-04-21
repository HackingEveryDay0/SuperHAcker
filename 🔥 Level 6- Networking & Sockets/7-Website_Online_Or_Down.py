# Write a script that checks if a website is online or down.

from urllib import request, error

try:
    with request.urlopen(" https://httpstat.us/404") as res:
        if res.getcode() == 200:
            print("Website is UP")
        else:
            print(f"Website Returned Status code: {res.getcode()}")
except error.HTTPError as e:
    print(e)
