# -*- coding: utf-8 -*-
"""https://stackoverflow.com/questions/36837594/get-scrapy-spider-to-crawl-entire-site"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os

class MySpider(CrawlSpider):
    name = 'wikileaks'
    allowed_domains = ['wikileaks.org']
    start_urls = ['https://wikileaks.org']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        print ("#"*50)
        url = response
        # print (type(url))
        # print(url)
        url = str(url)
        url_length = len(url)
        # print (type(url))
        # print(url)
        url = url.replace('<200 ', '')
        url = url.replace('>', '')
        print (url)
        file_full_path = getcwd()+"/Users/jack/Documents/GitHub/my_source_code/tools/python/crawling/scrapy/get_links_through_body_search/crawled_links.txt"
        with open(file_full_path, 'a') as f:
            f.write(url)
            f.write("\n")
        print ("*"*url_length)
        print ("\n\n\n")
