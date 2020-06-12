from scrapy import  cmdline
#第一步先从西刺代理中获取可用的代理服务器，保存到Redis中。
#cmdline.execute("scrapy crawl xici  -a url=https://www.qidian.com/".split())
#使用代理服务器执行爬虫
cmdline.execute("scrapy crawl hot".split())