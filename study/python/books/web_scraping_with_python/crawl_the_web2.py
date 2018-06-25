from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://www.hamyeondoinda.com/jack_wiki/doku.php"+pageUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	#Finds all links that begin with a "/"
	for link in bsObj.findAll("a", href=re.compile("^(/jack_wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# encouted a new page
				newPage = link.attrs['href']
				# print("-----------------\n"+newPage)

				if ".pdf" in newPage:
					print("OK external pdf link is: "+newPage)
				elif ".docx" in newPage:
					print("OK external docx link is: "+newPage)
				elif ".pptx" in newPage:
					print("OK external pptx link is: "+newPage)
				elif ".xlsx" in newPage:
					print("OK external xlsx link is: "+newPage)
				elif ".txt" in newPage:
					print("OK external txt link is: "+newPage)
				else:
					# print("XXX non target external link is: "+newPage)
					pass

				pages.add(newPage)
				getLinks(newPage)

getLinks("")