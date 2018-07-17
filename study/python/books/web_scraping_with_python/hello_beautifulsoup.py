from urllib.request import urlopen ### python3
# from urllib import urlopen ### python2
from bs4 import BeautifulSoup

target_url = "https://www.yahoo.co.jp"
html = urlopen(target_url)
bsObj = BeautifulSoup(html.read(), "html.parser")

# print(bsObj.h1)
print(bsObj)
