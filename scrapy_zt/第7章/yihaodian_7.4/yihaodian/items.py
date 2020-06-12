# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class YihaodianItem(scrapy.Item):
    price = scrapy.Field()#价格
    title = scrapy.Field()#标题
    positiveRatio = scrapy.Field()#好评率
    storeName = scrapy.Field()#店铺名称