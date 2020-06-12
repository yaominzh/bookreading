# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SeabornFileDownloadItem(scrapy.Item):
    file_urls = scrapy.Field()#文件url地址
    files = scrapy.Field()#文件下载信息
