from pyquery import PyQuery

html = """
    <li class="bbb"><a href="http://www.yuanlai.com">猿来</a></li>
"""

p = PyQuery(html)
href = p(".bbb a").attr("href")
print(href)
