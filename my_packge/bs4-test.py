from bs4 import BeautifulSoup

html = """
<ul>
<li><a href="zhangwuji.com">张无忌</a></li>
</ul>

"""
page = BeautifulSoup(html, 'html.parser')
li = page.find("a", attrs={"href": "zhangwuji.com"})
print(li.text)
