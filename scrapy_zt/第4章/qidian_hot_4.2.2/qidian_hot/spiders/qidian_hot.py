#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from qidian_hot.items import QidianHotItem#导入模块
from scrapy.loader import ItemLoader#导入ItemLoader类
class HotSalesSpider(Spider):
    #定义爬虫名称
    name = 'hot'
    #获取初始Request
    def start_requests(self):
        url = "https://www.qidian.com/rank/hotsales?style=1"
        #生成请求对象，设置url，headers，callback
        yield Request(url,callback=self.qidian_parse)
    # 数据解析函数
    def qidian_parse(self, response):
        #使用xpath定位到小说内容的div元素，保存到列表中
        list_selector = response.xpath("//div[@class='book-mid-info']")
        #依次读取每部小说的元素，从中获取名称、作者、类型和形式
        for one_selector in list_selector:
            #生成ItemLoader的实例
            #参数item接收QidianHotItem实例，selector接收一个接收器
            novel = ItemLoader(item=QidianHotItem(),selector=one_selector)
            #使用xpath选择器获取小说名称
            novel.add_xpath("name","h4/a/text()")
            #使用xpath选择器获取作者
            novel.add_xpath("author","p[1]/a[1]/text()")
            #使用xpath选择器获取类型
            novel.add_xpath("type","p[1]/a[2]/text()")
            #使用css选择器获取小说形式（连载还是完本）
            novel.add_css("form",".author span::text")
            #将提取好的数据load出来，并使用yield返回
            yield novel.load_item()