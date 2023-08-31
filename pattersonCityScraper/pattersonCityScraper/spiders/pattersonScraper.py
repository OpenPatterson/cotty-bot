import scrapy
from urllib.parse import urljoin

class QuotesSpider(scrapy.Spider):
    name = "patterson"
    allowed_domains = ["patterson.ca.us"]
    start_urls = ["https://ci.patterson.ca.us/",]

    def parse(self, response):
        print('A response just arrived from:', response.url)
        links = response.css('a::attr(href)').getall()
        file = open('pattersonLinks.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        if links is not None:
            for link in links:
                if link[0] == '#':
                    continue
                else:
                    yield scrapy.Request(url=urljoin('https://ci.patterson.ca.us/', link), callback=self.parse)
