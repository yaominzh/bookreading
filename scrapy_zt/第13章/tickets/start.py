from scrapy import  cmdline
#1.获取站点
#cmdline.execute("scrapy crawl sites".split())
#2.执行抢票功能
cmdline.execute("scrapy crawl tickets".split())
