# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DoubanItem(scrapy.Item):
    title = scrapy.Field()#电影名称
    directors = scrapy.Field()#导演
    casts = scrapy.Field()#演员
    rate = scrapy.Field()#评分

