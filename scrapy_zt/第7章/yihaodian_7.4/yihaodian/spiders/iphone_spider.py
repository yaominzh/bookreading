from scrapy import Request
from scrapy.spiders import Spider
from yihaodian.items import YihaodianItem#导入Item模块
from scrapy_splash import SplashRequest#导入SplashRequest模块
# splash lua script
lua_script = """
     function main(splash, args)
         splash:go(args.url)
         splash:wait(args.wait)
         splash:runjs("document.getElementsByClassName('mod_turn_page clearfix mt20')[0].scrollIntoView(true)")
         splash:wait(args.wait)
         return splash:html()
     end
     """
class PhoneSpider(Spider):
    name = 'iphone'#定义爬虫名称
    url = 'http://search.yhd.com/c0-0/kiphone/'#URL地址
    #获取初始Request
    def start_requests(self):
        yield SplashRequest(self.url,
                            callback=self.parse,
                            endpoint='execute',#Splash服务接口，执行lua脚本
                            args={'lua_source':lua_script,#lua source
                                  'images':0,#不显示图片
                                  'wait':3},#等待时间
                            cache_args=['lua_source'])#缓存
    # 数据解析
    def parse(self, response):
        item = YihaodianItem()#定义Item对象
        list_selector = response.xpath("//div[@class='itemBox']")
        for one_selector in list_selector:
            try:
                #价格
                price = one_selector.xpath(".//em[@class='num']/text()").extract()[-1]
                #去掉两边的换行符，空格等
                price = price.strip("\n\t")
                #标题
                title = one_selector.xpath("p[@class='proName clearfix']/a/text()").extract()[-1]
                # 去掉两边的换行符，空格等
                title = title.strip("\n\t    \t")
                #好评率
                positiveRatio = one_selector.xpath(".//span[@class='positiveRatio']/text()").extract()[0]
                #店铺名称
                storeName = one_selector.xpath(".//span[@class='shop_text']/text()").extract()[0]
                item["price"] = price
                item["title"] = title
                item["positiveRatio"] = positiveRatio
                item["storeName"] = storeName
                yield item
            except:
                 continue
        #获取下一页URL
        next_url = response.xpath("//a[@class='page_next']/@href").extract_first()
        if next_url:
            next_url = response.urljoin(next_url)#构建完整的URL
            #下一页的请求
            yield SplashRequest(next_url,
                                callback=self.parse,
                                endpoint='execute',
                                args={'lua_source':lua_script,'images':0,'wait':3})

