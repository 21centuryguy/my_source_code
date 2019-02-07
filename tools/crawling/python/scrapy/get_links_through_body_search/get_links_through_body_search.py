# -*- coding: utf-8 -*-
"""https://stackoverflow.com/questions/36837594/get-scrapy-spider-to-crawl-entire-site"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class MySpider(CrawlSpider):
    name = 'wikileaks'
    allowed_domains = ['wikileaks.org']
    start_urls = ['https://search.wikileaks.org/?q=future+job']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print ("#"*50)
        
        ########################
        url = response
        
        contents = response.body
        contents = str(contents)
        ########################

        if 'future job' in contents or 'Future Job' in contents or 'Future job' in contents:
            # print (type(url))
            print(url)
            url = str(url)
            url_length = len(url)
            # print (type(url))
            # print(url)
            url = url.replace('<200 ', '')
            url = url.replace('>', '')
            print (url)
            with open('/Users/jack/Documents/GitHub/my_source_code/tools/python/crawling/scrapy_urllib_bs4/scrapy/web_crawler/get_links_through_body_search/all_links_through_body_search.txt', 'a') as f:
                f.write(url)
                f.write("\n")
            print ("*"*url_length)
            print ("\n\n\n")
        else:
            print('-_-;'*20)
            print (url)
            print('no match')
            print('-_-;'*20)
            pass
