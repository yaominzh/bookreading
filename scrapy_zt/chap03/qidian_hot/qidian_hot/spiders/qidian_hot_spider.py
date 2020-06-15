# -*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider
import re


class HotSalesSpider(Spider):
    # 定义爬虫名称
    name = 'hot'
    # 起始的URL列表
    start_urls = ["http://tongbu.eduyun.cn/tbkt/tbktxx3yuwen/index.html"]

    # 解析函数
    def parse(self, response):
        hot_dict = {}
        list_selector = response.xpath("//div[@class='DanYuan']")
        for one_selector in list_selector:
            name = one_selector.xpath("h2/text()").extract()[0]
            name = name.strip()
            name = re.sub(r'\s|\"', '', name)
            hot_dict = {"name": name,
                        }
            # 使用yield返回字典
            yield hot_dict

        list_selector = response.xpath("//div[@class='DanYuan DanYuan1']")
        for one_selector in list_selector:
            name = one_selector.xpath("h2/text()").extract()[0]
            hot_dict = {"name": name,
                        }
            # 使用yield返回字典
            yield hot_dict
