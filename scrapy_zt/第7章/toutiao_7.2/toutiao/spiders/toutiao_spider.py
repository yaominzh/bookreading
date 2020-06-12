from scrapy import Request
from scrapy.spiders import Spider
from toutiao.items import ToutiaoItem#导入Item模块
from selenium import webdriver#导入浏览器引擎模块
class ToutiaoSpider(Spider):
    #定义爬虫名称
    name = 'toutiao'
    #构造函数
    def __init__(self):
        #创建PhantomJS的对象driver
        self.driver = webdriver.PhantomJS()
    #获取初始Request
    def start_requests(self):
        url = "https://www.toutiao.com/ch/news_hot/"
        #生成请求对象，设置url
        yield Request(url)
    # 数据解析
    def parse(self, response):
        item = ToutiaoItem()
        list_selector = response.xpath("//div[@class='wcommonFeed']/ul/li")
        for li in list_selector:
            try:
                #标题
                title = li.xpath(".//a[@class='link title']/text()").extract()
                #去除空格
                title = title[0].strip(" ")
                #来源
                source = li.xpath(".//a[@class='lbtn source']/text()").extract()
                #去除点号和全角空格
                source = source[0].strip("⋅").strip(" ")
                #评论数
                comment = li.xpath(".//a[@class='lbtn comment']/text()")
                #去除文字及空格
                comment = comment.re("(.*?)评论")[0]
                comment = "".join(comment.split())#去除空格：&nbsp
                item["title"] = title#标题
                item["source"] = source#来源
                item["comment"] = comment#评论数
                yield item
            except:
                continue
