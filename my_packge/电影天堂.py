import requests
import re

proxies = {
    "http": "http://127.0.0.1:33210",
    "https": "http://127.0.0.1:33210",
}

url = "https://dy2018.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# 取2023所有内容
resp = requests.get(url, headers=headers, proxies=proxies)
resp.encoding = 'gbk'
obj = resp.text

reg = re.compile(
    r'2023必看热片.*?<ul>(?P<html>.*?)</ul>',
    re.S)

result = reg.search(obj)
result1 = result.group('html')

# 取href
reg1 = re.compile(r"<li><a href='(?P<href>.*?)' title", re.S)
for i in reg1.finditer(result1):
    childUrl = url.strip("/") + i.group('href')
    childResp = requests.get(childUrl, headers=headers, proxies=proxies)
    childResp.encoding = 'gbk'
    print(childResp.text)
