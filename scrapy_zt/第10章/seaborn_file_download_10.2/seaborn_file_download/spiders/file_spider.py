#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from seaborn_file_download.items import SeabornFileDownloadItem#导入Item
class FileDownloadSpider(Spider):
    #定义爬虫名称
    name = 'file'
    #获取初始Request
    def start_requests(self):
        url = "http://seaborn.pydata.org/examples/index.html"
        #生成请求对象，设置url，headers，callback
        yield Request(url)

    # 解析函数-获取案例列表中每个案例的url地址
    def parse(self, response):
        #使用xpath定位到每个案例图片
        urls = response.xpath("//div[@class='figure align-center']/a/@href").extract()
        #遍历每个案例的url
        for i in range(len(urls)):
            # urljoin构建完整的url绝对地址
            url = response.urljoin(urls[i])
            #使用url构造Request请求，并返回
            yield Request(url,callback=self.parse_file)

    #解析函数-获取源码文件的url，将其放入key为file_urls的Item中
    def parse_file(self,response):
        #获取源文件的url地址
        href = response.xpath("//a[@class='reference download internal']/@href").extract_first()
        url = response.urljoin(href)
        #创建SeabornFileDownloadItem对象
        item = SeabornFileDownloadItem()
        #将源文件的url地址以列表的形式保存到key为file_urls的Item中
        item["file_urls"] = [url]
        yield item

