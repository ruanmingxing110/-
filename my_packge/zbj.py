import requests
from lxml import etree

proxies = {
    "http": "http://127.0.0.1:33210",
    "https": "http://127.0.0.1:33210",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

url = "https://www.zbj.com/search/service/?kw=saas&r=2"
res = requests.get(url, headers=headers, proxies=proxies)
res.encoding = "utf-8"

et = etree.htmlfile(res.text)
divs = et.xpath("//div[@class='search-result-list-service']/")
for i in divs:
    print()
