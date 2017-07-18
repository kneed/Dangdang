# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem

class DdpythonSpider(scrapy.Spider):
    name = 'ddpython'
    #allowed_domains = ['http://search.dangdang.com/?key=python']
    start_urls = ['http://search.dangdang.com/?key=python&act=input']

    def parse(self, response):
        #抓取各书本信息
        item=DangdangItem()
        item['name_']=response.xpath('//li//a/img/@alt').extract()
        item['summary_']=response.xpath('//p[@class="name"]/a/@title').extract()
        item['address_']=response.xpath('//p[@class="name"]/a/@href').extract()
        #item['author_']=response.xpath('//p[@class="search_book_author"]/span[1]/text()').extract()
        #item['publisher_']=response.xpath('//p[@class="search_book_author"]/span[3]/a/text()').extract()
        item['price_']=response.xpath('//p[@class="price"]/span[1]/text()').extract()
        print(len(item['name_']),len(item['summary_']),len(item['address_']),len(item['price_']))
        yield item

        next_url=response.xpath('//li[@class="next"]/a/@href').extract_first()
        if(next_url):
            yield scrapy.Request(response.urljoin(next_url),callback=self.parse)

