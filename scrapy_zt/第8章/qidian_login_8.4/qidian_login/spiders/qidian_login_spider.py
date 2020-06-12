# coding:utf-8
from scrapy import Request
from scrapy.spiders import Spider
from qidian_login.items import QidianLoginItem
import browsercookie#导入获取Cookie的库
class qidianSpider(Spider):
    name = 'bookshelf'#爬虫名称
    # 构造函数
    def __init__(self):
        cookiejar = browsercookie.chrome()#获取Chrome浏览器中的Cookie
        self.cookie_dict = {}#字典：保存起点中文网的Cookie
        # 遍历Chrome中所有的Cookie，获取起点中文网的Cookie
        for cookie in cookiejar:
            if cookie.domain == ".qidian.com":#域名为起点中文网
                if cookie.name in ["_csrfToken",
                                   "e1",
                                   "e2",
                                   "newstatisticUUID",
                                   "ywguid",
                                   "ywkey"] :
                    self.cookie_dict[cookie.name] = cookie.value
    # 初始请求函数
    def start_requests(self):
        url="https://my.qidian.com/bookcase" #初始网址
        yield Request(url,cookies=self.cookie_dict)#HTTP请求时，附加Cookie
    #数据解析函数
    def parse(self, response):
        item = QidianLoginItem()#Item对象
        tr_selector = response.xpath("//table[@id='shelfTable']/tbody/tr")
        for tr in tr_selector:
            category = tr.xpath("td[@class='col2']/span/b/a[1]/text()") #类型
            category = category.re("「(.*?)」")[0]#去掉类型两边的“「”和“」”
            title = tr.xpath("td[@class='col2']/span/b/a[2]/text()").extract()[0] #名称
            update = tr.xpath("td[@class='col3 font12']/text()").extract()[0] #更新时间
            author = tr.xpath("td[@class='col4']/a/text()").extract()[0]  #作者
            item["category"] = category#类型
            item["title"] = title#名称
            item["update"] = update#更新时间
            item["author"] = author#作者
            yield item
