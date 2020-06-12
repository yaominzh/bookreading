# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class ShetuImageDownloadItem(scrapy.Item):
    title = scrapy.Field()#图片类型，用于设置文件夹名称
    image_urls = scrapy.Field()#图片URL地址
    images = scrapy.Field()    #图片下载信息
