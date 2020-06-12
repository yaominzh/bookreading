#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from qidian_hot.items import QidianHotItem#导入模块
from qidian_hot import settings#导入配置文件
import redis#导入redis库
class HotSalesSpider(Spider):
    #定义爬虫名称
    name = 'hot'
    current_page = 1#设置当前页，起始为1
    def __init__(self):
        # 获取配置文件中redis配置信息
        host = settings.REDIS_HOST  # 主机地址
        port = settings.REDIS_PORT  # 端口
        db_index = settings.REDIS_DB_INDEX  # 索引
        db_psd = settings.REDIS_PASSWORD  # 密码
        # 连接redis，得到一个连接对象
        self.db_conn = redis.StrictRedis(host=host, port=port, db=db_index,
                                         password=db_psd,decode_responses=True)
    #获取初始Request
    def start_requests(self):
        proxy = self.db_conn.srandmember("ip")#随机获取一个代理url
        print(proxy)
        url = "https://www.qidian.com/rank/hotsales?style=1"
        #生成请求对象，设置url
        yield Request(url,callback=self.qidian_parse,
                      errback=self.error_back,
                      meta={"proxy": proxy, "download_timeout": 10}
                      )
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
            #将爬取到的一部小说保存到item中
            item = QidianHotItem() #定义QidianHotItem对象
            item["name"] = name    #小说名称
            item["author"] = author#作者
            item["type"] = type    #类型
            item["form"] = form    #形式
            #使用yield返回item
            yield item
        #获取下一页URL，并生成Request请求，提交给引擎
        #1.获取下一页URL
        self.current_page+=1
        if self.current_page<=25:
            next_url = "https://www.qidian.com/rank/hotsales?style=1&page=%d"%(self.current_page)
            proxy = self.db_conn.srandmember("ip")  # 随机获取一个代理url
            print(proxy)
            #2.根据URL生成Request，使用yield返回给引擎
            yield Request(next_url,
                          callback=self.qidian_parse,
                          errback=self.error_back,
                          meta={"proxy": proxy, "download_timeout": 10},
                          )

    def error_back(self,failure):
        #打印错误日志信息
        self.logger.error(repr(failure))
        #获取请求request
        request = failure.request
        print("hahah:",request.meta["proxy"].upper())
        #从Redis中删除无效的代理，upper()功能为转换为大写字母
        self.db_conn.srem("ip",request.meta["proxy"].upper())
        # 随机获取一个代理url
        proxy = self.db_conn.srandmember("ip")
        print("重新选择代理URL：",proxy)
        #使用新的代理，重新请求
        yield Request(request.url,
                      callback=self.qidian_parse,
                      errback=self.error_back,
                      meta={"proxy":proxy,"download_timeout":10},
                      dont_filter=True)