# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#保存小说热销榜字段数据
class QidianHotItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  #小说名
    author = scrapy.Field()#作者
    type = scrapy.Field()  #类型
    form = scrapy.Field()  #形式

#保存一周推荐票榜数据
class WeekHotItem(QidianHotItem):
    content = scrapy.Field()  #内容

