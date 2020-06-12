#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from qidian_hot.items import XiciItem
from twisted.internet.error import DNSLookupError,TimeoutError, TCPTimedOutError#导入错误模块

class XiciSpider(Spider):
    name = 'xici'#爬虫名称
    current_page = 1#当前页
    def __init__(self,url):
        self.test_url = url#从命令中获取测试网站的url

    #获取初始Request
    def start_requests(self):
        url = "https://www.xicidaili.com/nn"#西祠代理免费代理的url地址
        #生成请求对象
        yield Request(url)
    # 数据解析
    def parse(self, response):
        list_selector = response.xpath("//tr[@class='odd']")
        #依次读取每条代理的信息，从中获取ip、端口、类型
        for one_selector in list_selector:
            item = XiciItem()#Item对象
            #获取ip
            ip = one_selector.xpath("td[2]/text()").extract()[0]
            #获取端口
            port =  one_selector.xpath("td[3]/text()").extract()[0]
            #获取是否高匿
            cryptonym = one_selector.xpath("td[5]/text()").extract()[0]
            #获取类型（http或https）
            http = one_selector.xpath("td[6]/text()").extract()[0]
            #拼接成完整的代理url
            url = "{}://{}:{}".format(http,ip,port)
            item["url"] = url
            #一定要设置dont_filter=True不过滤重复请求
            yield Request(self.test_url,#测试网站的url
                          callback=self.test_parse,#回调函数
                          errback=self.error_back,#出错回调函数
                          meta={"proxy":url,#代理服务器地址
                                "dont_retry":True,#请求不重试
                                "download_timeout":10,#超时时间
                                "item":item},
                          dont_filter=True#不过滤重复请求
                          )
        if self.current_page <= 5:#爬取5页代理信息
            #获取下一页url
            next_url = response.xpath("//a[@class='next_page']/@href").extract()[0]
            next_url = response.urljoin(next_url)
            self.current_page+=1
            yield Request(next_url)

    # 测试网站的数据解析
    def test_parse(self, response):
        yield response.meta["item"]
    #请求失败的回调函数
    def error_back(self,failure):
        #打印错误日志信息
        self.logger.error(repr(failure))
        #细化出错原因
        if failure.check(DNSLookupError):# DNS出错
            # 获取request
            request = failure.request
            #输出错误日志信息
            self.logger.error('DNSLookupError on %s', request.url)
        elif failure.check(TimeoutError, TCPTimedOutError):#超时出错
            # 获取request
            request = failure.request
            #输出错误日志信息
            self.logger.error('TimeoutError on %s', request.url)