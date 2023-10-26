import requests

url = 'https://www.bizhi99.com/index/statistics/index.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Referer": "https://www.bizhi99.com/c2/",
    "Host": "www.bizhi99.com",
    "Cookie": "bizhi99_visitorId=651f63a7d17a0",
    "Origin": "https://www.bizhi99.com"
}

response = requests.get(url=url, headers=headers)
print(response.text)
