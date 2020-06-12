from scrapy import  cmdline

cmdline.execute("scrapy crawl bookshelf -o bookshelf.csv".split())
