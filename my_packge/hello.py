import requests
import re

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
obj = resp.text

reg = re.compile(
    r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?导演: (?P<director>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;',
    re.S)
result = reg.finditer(obj)
for i in result:
    name = i.group("name")
    director = i.group("director")
    rating = i.group("rating")
    year = i.group("year").strip()

    print(name, director, rating, year)
