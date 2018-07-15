# -*- coding: utf-8 -*-
####
# https://stackoverflow.com/questions/28774852/pypi-api-how-to-get-stable-package-version

# import requests
import json
import sys, os
from urllib.request import urlopen
from bs4 import BeautifulSoup
os.environ['PYTHONIOENCODING'] = 'UTF-8'

try:
	from packaging.version import parse
except ImportError:
	from pip._vendor.packaging.version import parse

req = request.get('https://pypi.python.org/pypi/Django/json')

req2 = request.get('https://www.google.com')

print (req)

print (req2)
