# -*- coding: utf-8 -*-
"""https://stackoverflow.com/questions/36837594/get-scrapy-spider-to-crawl-entire-site"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.request import urlopen ### python3
from bs4 import BeautifulSoup

class MySpider(CrawlSpider):
    # name = 'intra-mart'
    # allowed_domains = ['intra-mart.jp']
    # start_urls = ['https://www.intra-mart.jp']

    name = 'google news'
    allowed_domains = ['news.google.com']
    start_urls = ['https://news.google.com']

    # name = 'google.com'
    # allowed_domains = ['google.com']
    # start_urls = ['https://www.google.com']    

    #################################################################################

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        # print ("#"*50)
        xxx = response
        # print (type(xxx))
        # print(xxx)
        xxx = str(xxx)
        url_length = len(xxx)
        # print (type(xxx))
        # print(xxx)
        xxx = xxx.replace('<200 ', '')
        xxx = xxx.replace('>', '')

    #################################################################################

        html = urlopen(xxx)
        soup = BeautifulSoup(html, "html.parser")
        content = soup.get_text()
        # content = soup.find_all('div')
        # content = soup.find_all('a', href=True)        
        # print(type(content))
        content = str(content)
        # print(type(content))
        # print ("1"*50)
        # print (xxx)
        # print (content)
        # print ("9"*50)
        # print ("\n\n\n")

    #################################################################################

        # if 'future job' in content:
        if 1 == 1:
            print ("#"*50)
            print (xxx)
            print (content)
            import os
            file_full_path = "/Users/jack/Documents/GitHub/my_source_code/tools/python/crawling/scrapy_urllib_bs4/scrapy/web_crawler/crawled_links.txt"
            with open(file_full_path, 'a') as f:
                f.write(xxx)
                f.write("\n")
            print ("*"*url_length)
            print ("\n\n\n")
        else:
            print('-_-;'*20)
            print (xxx)
            print('no match')
            print('-_-;'*20)
            pass
