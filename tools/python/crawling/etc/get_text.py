# from urllib.request import urlopen ### python3
from urllib import urlopen ### python2
from bs4 import BeautifulSoup

html = urlopen('http://www.hamyeondoinda.com')
# print html
soup = BeautifulSoup(html, "html.parser")
# print soup
xxx = soup.get_text()
print xxx
