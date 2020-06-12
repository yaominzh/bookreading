# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanLoginItem(scrapy.Item):
    title = scrapy.Field()#书名
    author = scrapy.Field()#作者
    publishing_house = scrapy.Field()#出版社
    publish_time = scrapy.Field()#出版时间
