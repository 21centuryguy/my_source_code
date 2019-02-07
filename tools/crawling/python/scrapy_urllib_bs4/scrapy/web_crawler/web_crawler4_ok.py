# -*- coding: utf-8 -*-
"""https://stackoverflow.com/questions/36837594/get-scrapy-spider-to-crawl-entire-site"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.request import urlopen ### python3
from bs4 import BeautifulSoup
import os

class MySpider(CrawlSpider):
    name = 'wikileaks'
    allowed_domains = ['wikileaks.org']
    start_urls = ['https://search.wikileaks.org/?q=korea']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        print ("#"*50)
        xxx = response
        # print (type(xxx))
        # print(xxx)
        xxx = str(xxx)
        url_length = len(xxx)
        # print (type(xxx))
        # print(xxx)
        xxx = xxx.replace('<200 ', '')
        xxx = xxx.replace('>', '')
        html = urlopen(xxx)
        soup = BeautifulSoup(html, "html.parser")
        content = soup.get_text()
        if 'Korea' in content or 'korea' in content:
            print (xxx)
            file_full_path = getcwd()+"/Users/jack/Documents/GitHub/my_source_code/tools/python/crawling/scrapy_urllib_bs4/scrapy/web_crawler/crawled_links.txt"
            with open(file_full_path, 'a') as f:
                f.write(xxx)
                f.write("\n")
            print ("*"*url_length)
            print ("\n\n\n")
        else:
            pass
