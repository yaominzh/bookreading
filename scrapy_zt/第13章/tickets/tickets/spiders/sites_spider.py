from scrapy.spiders import Spider
from scrapy import Request
import re
import os
class SitesSpider(Spider):
    name = "sites"
    def start_requests(self):
        # 获取站点信息的URL
        url = 'https://kyfw.12306.cn/otn/resources/' \
              'js/framework/station_name.js?station_version=1.9040'
        yield Request(url)

    def parse(self, response):
        #使用正则表达式获取站点名和站点编码
        #\u4e00-\u9fa5为unicode格式的汉字编码范围
        #字符串前的r用于防止字符转义，如\n就不会转义为换行符
        sites = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
        # 如果站点文件存在，则删除该文件
        if(os.path.exists("sites.txt")):
            os.remove("sites.txt")
        #将站点信息保存到文件中
        with open("sites.txt","a",encoding="utf-8") as f:
            for site_name, site_code in sites:
                # 以“站点名:站点编码”的形式保存到文件
                f.write(site_name+":"+site_code+"\n")