from urllib.request import urlopen
from bs4 import BeautifulSoup

target_url = "https://www.yahoo.co.jp"
html = urlopen(target_url)
bsObj = BeautifulSoup(html.read(), "html.parser")

# print(bsObj.h1)
print(bsObj)
