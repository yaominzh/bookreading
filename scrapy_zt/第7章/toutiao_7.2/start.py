from scrapy import  cmdline

cmdline.execute("scrapy crawl toutiao -o toutiao.csv".split())
