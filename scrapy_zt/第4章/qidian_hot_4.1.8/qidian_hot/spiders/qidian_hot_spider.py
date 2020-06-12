#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
class HotSalesSpider(Spider):
    #定义爬虫名称
    name = 'hot'
    current_page = 1#设置当前页，起始为1
    #获取初始Request
    def start_requests(self):
        url = "https://www.qidian.com/rank/hotsales?style=1"
        #生成请求对象，设置url，callback
        yield Request(url,callback=self.qidian_parse)
    # 解析数据
    def qidian_parse(self, response):
        #使用xpath定位到小说内容的div元素，保存到列表中
        list_selector = response.xpath("//div[@class='book-mid-info']")
        #依次读取每部小说的元素，从中获取名称、作者、类型和形式
        for one_selector in list_selector:
            #获取小说名称
            name = one_selector.xpath("h4/a/text()").extract_first()
            #获取作者
            author = one_selector.xpath("p[1]/a[1]/text()").extract()[0]
            #获取类型
            type = one_selector.xpath("p[1]/a[2]/text()").extract()[0]
            #获取形式（连载还是完本）
            form = one_selector.xpath("p[1]/span/text()").extract()[0]
            #将爬取到的一部小说保存到字典中
            hot_dict = {"name":name,         #小说名称
                        "author":author,     #作者
                        "type":type,         #类型
                        "form":form}         #形式
            #使用yield返回字典
            yield hot_dict
        #获取下一页URL，并生成Request请求，提交给引擎
        #1.获取下一页URL
        self.current_page+=1
        if self.current_page<=25:
            next_url = "https://www.qidian.com/rank/hotsales?style=1&page=%d"%(self.current_page)
            #2.根据URL生成Request，使用yield返回给引擎
            yield Request(next_url,callback=self.qidian_parse)