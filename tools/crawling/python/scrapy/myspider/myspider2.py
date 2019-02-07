import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    def parse_page1(self, response):
    	return scrapy.Request("http://www.hamyeondoinda.com/index.html", callback=self.index.html)
