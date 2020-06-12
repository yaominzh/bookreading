# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class ToutiaoItem(scrapy.Item):
    title = scrapy.Field()#标题
    source = scrapy.Field()#来源
    comment = scrapy.Field()#评论数

