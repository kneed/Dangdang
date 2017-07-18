# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_=scrapy.Field()
    summary_=scrapy.Field()
    address_=scrapy.Field()
    #author_=scrapy.Field()
    #publisher_=scrapy.Field()
    price_=scrapy.Field()
