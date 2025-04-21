# 6.​ Create a program that sends fake HTTP headers to mimic different browsers.

from urllib import request, error


missing_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "Referer":"https://www.google.com/",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

try:
    req_params = request.Request(url="https://httpbin.io/headers",headers=missing_headers)

    req = request.urlopen(req_params).read()


    print(req.decode('utf-8'))

except error.HTTPError as e:
    print(e)
