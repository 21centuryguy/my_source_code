def py37_urllib():
	# urllib ( python3.7 )
	# https://docs.python.org/3.7/library/urllib.request.html
	import urllib
	import requests
	urllib.request.urlopen("https://google.com")

def py27_urllib():
	# urllib ( python 2.7 )
	# https://docs.python.org/2.7/library/urllib.html#module-urllib
	import urllib
	urllib.urlopen("https://google.com")

def py27_urllib2():
	# urllib2 ( python2.7 )
	# https://docs.python.org/2.7/library/urllib2.html?highlight=urlopen#urllib2.urlopen
	import urllib2
	urllib2.urlopen("https://google.com")

def py37_requests():
	# requests ( python 2, 3)
	# http://docs.python-requests.org/en/latest/index.html
	import requests
	requests.get("https://google.com")


py37_urllib()
# py27_urllib()
# py27_urllib2()
# py37_requests()
