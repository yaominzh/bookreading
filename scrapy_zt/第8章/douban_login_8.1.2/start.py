from scrapy import  cmdline

cmdline.execute("scrapy crawl login -o doulist.csv".split())
