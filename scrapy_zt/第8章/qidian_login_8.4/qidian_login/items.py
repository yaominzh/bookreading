# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class QidianLoginItem(scrapy.Item):
    category = scrapy.Field()#类型
    title    = scrapy.Field()#名称
    update   = scrapy.Field()#更新时间
    author   = scrapy.Field()#作者
