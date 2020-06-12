# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time#导入时间模块
from scrapy.http import HtmlResponse#导入html响应模块
from selenium.webdriver.common.by import By#导入By模块
from selenium.webdriver.support.wait import WebDriverWait#导入等待模块
from selenium.webdriver.support import expected_conditions as EC#导入预期条件模块
from selenium.common.exceptions import TimeoutException, NoSuchElementException#异常模块
class ToutiaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ToutiaoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        #判断name是toutiao的爬虫
        if spider.name == "toutiao":
            #打开URL对应的页面
            spider.driver.get(request.url)
            try:
                #设置显式等待,最长等待5秒
                wait = WebDriverWait(spider.driver, 5)
                #等待新闻列表容器加载完成
                wait.until(EC.presence_of_element_located(
                    (By.XPATH,"//div[@class='wcommonFeed']")))
                # 使用js的scrollTo方法实现将页面向下滚动到中间
                spider.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/2)')
                for i in range(10):
                    time.sleep(5)
                    # 使用js的scrollTo方法将页面滚动到最底端
                    spider.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                #获取加载完成的页面源代码
                origin_code = spider.driver.page_source
                # 将源代码构造成为一个Response对象，并返回。
                res = HtmlResponse(url=request.url, encoding='utf8', body=origin_code, request=request)
                return res
            except TimeoutException:#超时
                print("time out")
            except NoSuchElementException:#无此元素
                print("no such element")
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
