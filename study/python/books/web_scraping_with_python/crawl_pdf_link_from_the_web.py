from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html.read(), "html.parser")

	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# encouted a new page
				newPage = link.attrs['href']
				pages.add(newPage)
				if ".pdf" in newPage:
					print("-----------------\n"+newPage)
				else:
					pass
					print('not pdf link')
				getLinks(newPage)
getLinks("")